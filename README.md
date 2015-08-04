# Tournament Planner
## Purpose
Completed as part of Project 2 for the Udacity Full Stack Nonodegree.

## Requirements
1.  [Vagrant](https://www.vagrantup.com/)
1.  [VirtualBox](https://www.virtualbox.org/)

## Usage
1.  Clone repository: ```git clone https://github.com/wduncanfraser/tournament_planner.git```.
1.  Run ```vagrant up``` and then ```vagrant ssh``` to provision and log into the vm.
1.  Once logged into the VM, run ```python tournament_test.py``` to run the unit tests for the tournament planner.

## Structure
+   Vagrantfile: Vagrant VM configuration.
+   pg_config.sh: Provisioning script for the Vagrant VM. Installs the desired packages and configures the tournament database.
+   tournament.sql: SQL definitions for the database schema.
+   tournament.py: Function definitions for the tournament planner.
+   tournament_test.py: Unit tests for the tournament planner functions.

## Legal
Author: [W. Duncan Fraser](duncan@wduncanfraser.com)

License: [MIT License](LICENSE)