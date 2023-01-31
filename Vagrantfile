Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provider "virtualbox" do |vb|
      vb.name = "Mininet Wifi VM"
      vb.memory = "8192"
      vb.cpus = "2"
      vb.customize ['modifyvm', :id, '--vram', '64']
      vb.customize ['modifyvm', :id, '--graphicscontroller', 'vmsvga']
      vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.gui = true


  # Mininet Wifi
  config.vm.provision "shell",  path: "scripts/mininet-wifi.sh"

  # Add desktop environment
  config.vm.provision :shell, inline: "sudo apt install -y xfce4 virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11"

  # Add `vagrant` to Administrator
  config.vm.provision :shell, inline: "sudo usermod -a -G sudo vagrant"

  # Restart
  #config.vm.provision :shell, inline: "sudo shutdown -r now"

  end
end