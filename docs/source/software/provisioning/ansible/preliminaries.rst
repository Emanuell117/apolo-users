.. _ansible-preliminaries:

.. highlight:: rst

.. role:: bash(code)
   :language: bash

.. role:: raw-html(raw)
   :format: html

.. sidebar:: Contents

   .. contents::
      :local:

Inventory
---------------------

Ansible performs actions, also known as tasks, over a group of computers; in order to
do so it reads a plain text file called "inventory file" containing a list of
hostnames, or IP addresses, often grouped based on one or multiple shared features.

The inventory file is located by default under :bash:`/etc/ansible/hosts`
and would typically follow the conventions shown below:

#. Group names are delimited by :bash:`[` and :bash:`]`. e.g. group lbservers would be written as :bash:`[lbservers]`.
#. Hosts below a group definition are to be taken as members of it. e.g.

   .. code-block:: ini

      ; lbservers -> Group
      ; [host1,host2].example.com -> Members
      [lbservers]        
      host1.example.com
      host2.example.com

   .. figure:: src/images/inventory_example-1/inventory_example-1.png
      :alt: lbservers' components

#. Using the suffix :bash:`:children` within a group definition indicates the presence of
   nested groups (i.e. subgroups). e.g.

   .. code-block:: ini

      ; lbservers -> Group
      ; lb[south,north] -> Subgroups
      [lbservers:children]
      lbsouth
      lbnorth

   .. note::

      Subgroups are only declared as part of a parent-child relation
      (i.e. nesting depth is 1), thus implying that relations where
      nesting depth is greater than 1 require multiple declarations.

   .. code-block:: ini

      ; lbservers -> Grandparent
      ; lb[south,north] -> Children
      [lbservers:children]
      lbsouth
      lbnorth

      ; lbs[1,2].example.com -> Grandchildren
      [lbsouth:children]
      lbs1.example.com
      lbs2.example.com

#. The suffix :bash:`:vars` within a group definition is used to declare and assign
   variables to a particular set of hosts or subgroups. e.g.

   .. note::

      These variables are relative to group members and can be overwritten
      by subgroups and other ansible components (e.g. playbooks, tasks).

   .. code-block:: ini
	 
      ; lbsouth and lbnorth will inherit all
      ; variables declared within lbservers.
      [lbservers:children]
      lbsouth
      lbnorth

      [lbservers:vars]
      requests_timeout=5
      max_hosts_to_serve=10

      ; "requests_timeout" will be overwritten
      ; for lbsouth members only.
      [lbsouth:vars]
      requests_timeout=3

      ; Members of this group will not recognize
      ; variables declared for lbservers, as they
      ; do not belong to it.
      [backupservers]
      bk1.example.com
      bk2.example.com

   .. figure:: src/images/inventory_example-children/inventory_example-children.png
      :alt: lbservers' components
      
It is impotant to highlight that there are two default groups: :bash:`all` and
:bash:`ungrouped`, which, unlike any other group, can be omitted within the
inventory file, as their definitions are both implicit. Please be aware that: 

#. Hierarchically, all groups and hosts are members of :bash:`all`.

#. Hosts with no group other than all belong to :bash:`ungrouped`. Therefore, hosts
   will be members of at least two groups.

Hence, it is true for the examples above:

.. figure:: src/images/inventory_example-implicit/inventory_example-implicit.png
   :alt: lbservers' components

Playbooks
---------------------
A playbook is a text file containing information on which tasks to apply on which
hosts. This information is contained within a definition block called "Play". Take
the following playbook for example:

.. code-block:: yaml

   - hosts: lbsouth
     vars:
       nginx_conf_dir: /etc/nginx/

   - hosts: lbnorth
     vars:
       nginx_conf_dir: /opt/nginx/conf
		
   - hosts: lbservers
     vars:
       max_clients: 100
     tasks:
     - name: Install/update nginx
       yum:
         name: nginx
	 state: latest
     - name: Place nginx config file
       template:
         src: templates/nginx.conf.j2
	 dest: "{{ nginx_conf_dir }}/conf/nginx.conf"
       notify:
         - restart nginx
     - name: Ensure nginx is running
       systemd:
         name: nginx
	 state: started
	 enabled: true
     handlers:
       - name: restart nginx
	 systemctl:
	   name: nginx
	   state: restarted

Plays are separated by a non-printable '\n', thus there are three plays. Each one
uses the keyword "hosts" to describe a group, defined in the inventory file,
on which to apply some tasks and/or set variables.



Authors
---------------------

- Tomás Felipe Llano-Rios <tllanos@eafit.edu.co>
