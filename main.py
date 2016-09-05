'''
* Name: GTKSysInfo
* Version: 0.0.2 (PRERELEASE)
* File: main.py
* Description: Frontend system information for Linux GTK
* Contributors: id01 (main developer)
* Libraries used: 
'''
import gi;
gi.require_version("Gtk", "3.0");
import re;
import os;
import time;
from gi.repository import Gtk

# Move to directory that main.py is in
os.chdir(os.path.realpath("./" + "".join(__file__.rsplit('/', 1)[0])));

# Check if rooted
if os.system("bin/c/checkroot")!=0:
	rooted=False;
else:
	rooted=True;

# Define Variables

# Main window
class mainClass(Gtk.Window):
	
	def __init__(self):
### INIT
		# Initialize Window
		Gtk.Window.__init__(self, title="GTK System Info")
		Gtk.Window.set_size_request(self,800,400);
		# Define a box for vertical and horizontal
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		self.add(self.vbox);
		self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
		self.add(self.hbox);
### WARNING IF NO ROOT, ACTIVATE EXTRA FEATURES IF ROOTED
		if rooted==False:
			rootWarning = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Warning: No root")
			rootWarning.format_secondary_text("Some features may not work with limited previliges.");
			rootWarning.run();
			rootWarning.destroy();
		else:
			if os.system("mkdir /tmp/GTKSysInfo")!=0:
				if os.system("umount /tmp/GTKSysInfo; rmdir /tmp/GTKSysInfo")!=0:
					tmpWarning = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Directory Exists");
					tmpWarning.format_secondary_text("ERROR: /tmp/GTKSysInfo exists and may contain data. Did you create it or kill this task?");
					tmpWarning.run(); exit();
				else:
					os.system("mkdir /tmp/GTKSysInfo");

### STACK CONFIG
		# Define and configure a stack
		mainStack = Gtk.Stack();
		mainStack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		mainStack.set_transition_duration(500);
		# Within mainStack

### LAYER 1
		# Define First layer of Stack
		''' CREATING - LAYER 1 '''
		## Define and configure Grid for Disks
		self.diskGridScroll = Gtk.ScrolledWindow(hexpand=True, vexpand=True);
		self.diskGrid = Gtk.Grid(column_homogeneous=True, row_homogeneous=False, column_spacing=10, row_spacing=2)
		self.diskGrid.set_column_spacing(spacing=8);
		self.diskIndentLabel=Gtk.Label()
		self.diskIndentLabel.set_text("\t\t\t\t\t");
		self.add(self.diskGrid)
		## Disk Partitions
		self.diskPartGrid = Gtk.Grid()
		self.diskPartGrid.set_column_spacing(spacing=10);
		self.add(self.diskPartGrid)
		self.diskPartTypeLabel = Gtk.Label()
		self.diskPartNameLabel = Gtk.Label()
		self.diskPartFsLabel = Gtk.Label()
		self.diskPartSizeLabel = Gtk.Label()
		self.diskPartMountLabel = Gtk.Label()
		# Set align
		self.diskPartTypeLabel.set_valign(1)
		self.diskPartTypeLabel.set_halign(1)
		self.diskPartNameLabel.set_valign(1)
		self.diskPartNameLabel.set_halign(1)
		self.diskPartFsLabel.set_valign(1)
		self.diskPartFsLabel.set_halign(1)
		self.diskPartSizeLabel.set_valign(1)
		self.diskPartSizeLabel.set_halign(1)
		self.diskPartMountLabel.set_valign(1)
		self.diskPartMountLabel.set_halign(1)
		# Set text
		self.diskPartTypeLabel.set_text("TYPE:\nNO DISK SPECIFIED")
		self.diskPartNameLabel.set_text("PARTITIONS:\nNO DISK SPECIFIED")
		self.diskPartFsLabel.set_text("\n")
		self.diskPartSizeLabel.set_text("\n")
		self.diskPartMountLabel.set_text("\n")
		## Disk Types
		self.diskVendorLabel = Gtk.Label()
		self.diskVendorLabel.set_text("VENDOR:\nNO DISK SPECIFIED\n\nMODEL:\nNO DISK SPECIFIED")
		self.diskVendorLabel.set_valign(1)
		self.diskVendorLabel.set_halign(1)
		## Disk State/Hotplug/UUID
		self.diskStateLabel = Gtk.Label()
		self.diskStateLabel.set_text("HOTPLUGGABLE:\nNO DISK SPECIFIED\n\nRUNNING:\nNO DISK SPECIFIED\n\nUUID:\nNO DISK SPECIFIED")
		self.diskStateLabel.set_valign(1)
		self.diskStateLabel.set_halign(1)
		## Create button for each disk
		self.diskSelectGrid = Gtk.Grid()
		self.add(self.diskSelectGrid)
		self.diskAllGrid = Gtk.Grid()
		self.diskAllGrid.set_column_spacing(spacing=10);
		self.add(self.diskAllGrid)
		self.buttonList=[]
		for x in range(0,int(os.popen("lsblk -io NAME | grep -v '-' | grep -v 'NAME' | wc -l").read())):
			disknamevar=os.popen("lsblk -io NAME | grep -v '-' | grep -v 'NAME' | head -n " + str(x+1) + " | tail -n 1").read().rstrip();
			self.buttonList.append(Gtk.Button(label=disknamevar + "\n" + os.popen("lsblk -io SIZE /dev/" + disknamevar + " | head -n 2 | tail -n 1").read().strip()));
			print self.buttonList[x]
			self.buttonList[x].connect("clicked", self.change_text_disk, disknamevar)
			self.diskSelectGrid.attach(self.buttonList[x], 1, x+1, 1, 1)
		## Create Partition Select Entry
		self.partSelectLabel = Gtk.Label();
		self.partSelectLabel.set_text("Enter Mounted Partition\nHere To View Details:");
		self.partSelectLabel.set_halign(1);
		self.partSelectEntry = Gtk.Entry();
		self.partSelectEntry.set_text("sda1");
		self.partSelectEntry.connect('activate', self.change_part_text);
		self.diskSelectGrid.attach(self.partSelectLabel, 1, len(self.buttonList)+1, 1, 1);
		self.diskSelectGrid.attach(self.partSelectEntry, 1, len(self.buttonList)+2, 1, 1);
		## Create Partition Details
		self.partDetailsGrid = Gtk.Grid();
		self.add(self.partDetailsGrid);
		self.partDetailsLabel = Gtk.Label();
		self.partDetailsLabel.set_text("Partition Details:\n");
		self.partDetailsGrid.add(self.partDetailsLabel);
		## Create Partition Space Details
		self.partSpaceLabelStatic = Gtk.Label();
		self.partSpaceLabelStatic.set_text("Space used: ");
		self.partSpaceBar = Gtk.ProgressBar();
		self.partSpaceLabel = Gtk.Label();
		self.partSpaceLabel.set_text("Select Mounted Partition");
		self.partDetailsGrid.attach(self.partSpaceLabelStatic, 0, 1, 1, 1);
		self.partDetailsGrid.attach(self.partSpaceBar, 0, 2, 1, 1);
		self.partDetailsGrid.attach(self.partSpaceLabel, 0, 3, 1, 1);
		## Create Partition UUID Details
		self.partUUIDLabel = Gtk.Label()
		self.partUUIDLabel.set_text("\nUUID:\nNONE")
		self.partDetailsGrid.attach(self.partUUIDLabel, 0, 4, 1, 1);

		''' DRAWING - LAYER 1 '''
		## Add Disk Information Underneath Buttons
		self.diskPartGrid.add(self.diskPartNameLabel);
		self.diskPartGrid.add(self.diskPartFsLabel);
		self.diskPartGrid.add(self.diskPartSizeLabel);
		self.diskPartGrid.add(self.diskPartMountLabel);
		self.diskGrid.attach(self.diskPartTypeLabel, 0, 1, 1, 1);
		self.diskGrid.attach(self.diskIndentLabel, 0, 2, 1, 1);
		self.diskGrid.attach(self.diskPartGrid, 0, 2, 3, 1);
		self.diskGrid.attach(self.diskVendorLabel, 1, 1, 1, 1);
		self.diskGrid.attach(self.diskStateLabel, 2, 1, 1, 1);
		self.diskAllGrid.add(self.diskSelectGrid)
		self.diskAllGrid.add(self.diskGrid)
		self.diskAllGrid.attach(self.partDetailsGrid, 3, 0, 1, 1);
		## Add DiskGrid To Stack
		self.diskGridScroll.add(self.diskAllGrid);
		mainStack.add_titled(self.diskGridScroll, "Disks", "Disks");

### LAYER X
		''' CREATING - LAYER X '''
		## Scroll Container
		self.stressTestScroll = Gtk.ScrolledWindow(hexpand=True, vexpand=True);
		## Grid
		self.stressTestGrid=Gtk.Grid(column_homogeneous=True, row_homogeneous=False, column_spacing=10, row_spacing=2);
		self.add(self.stressTestGrid);
		## Labels
		# Create
		self.floatoperLabel=Gtk.Label();
		self.intoperLabel=Gtk.Label();
		self.floatoperLabelMulti=Gtk.Label();
		self.intoperLabelMulti=Gtk.Label();
		self.ramallocWriteLabel=Gtk.Label();
		self.ramallocReadLabel=Gtk.Label();
		self.randgenLabel=Gtk.Label();
		# Set Selectable
		self.floatoperLabel.set_selectable(True);
		self.intoperLabel.set_selectable(True);
		self.floatoperLabelMulti.set_selectable(True);
		self.intoperLabelMulti.set_selectable(True);
		self.ramallocWriteLabel.set_selectable(True);
		self.ramallocReadLabel.set_selectable(True);
		self.randgenLabel.set_selectable(True);
		# Buttons
		self.stressTestStartButton=Gtk.Button(label="Start Stress Test");
		self.stressTestStartButton.connect("clicked", self.stress_test);
		self.stressTestSaveButton=Gtk.Button(label="Save Results to File");
		self.stressTestSaveButton.connect("clicked", self.stress_test_save);
		# Set text
		self.floatoperLabel.set_text("Float Operations/Second (single-core): UNKNOWN\n");
		self.intoperLabel.set_text("Integer Operations/Second (single-core): UNKNOWN\n");
		self.floatoperLabelMulti.set_text("Float Operations/Second (multi-core): UNKNOWN\n");
		self.intoperLabelMulti.set_text("Integer Operations/Second (multi-core): UNKNOWN\n");
		self.randgenLabel.set_text("Random Numbers Generated/Second: UNKNOWN\n");
		self.ramallocWriteLabel.set_text("RAM Write Speed (Bps): UNKNOWN\n");
		self.ramallocReadLabel.set_text("RAM Read Speed (Bps): UNKNOWN\n");
		## Spinner
		self.stressTestSpinner = Gtk.Spinner();
		self.stressTestSpinner.stop();

		''' DRAWING - LAYER X '''
		self.stressTestGrid.attach(self.intoperLabel, 0, 1, 4, 1);
		self.stressTestGrid.attach(self.intoperLabelMulti, 0, 2, 4, 1);
		self.stressTestGrid.attach(self.floatoperLabel, 0, 3, 4, 1);
		self.stressTestGrid.attach(self.floatoperLabelMulti, 0, 4, 4, 1);
		self.stressTestGrid.attach(self.randgenLabel, 0, 5, 4, 1);
		self.stressTestGrid.attach(self.ramallocReadLabel, 0, 6, 4, 1);
		self.stressTestGrid.attach(self.ramallocWriteLabel, 0, 7, 4, 1);
		self.stressTestGrid.attach(self.stressTestStartButton, 0, 8, 1, 1);
		self.stressTestGrid.attach(self.stressTestSaveButton, 1, 8, 1, 1);
		self.stressTestGrid.attach(self.stressTestSpinner, 2, 8, 1, 1);
		self.stressTestScroll.add(self.stressTestGrid);
		mainStack.add_titled(self.stressTestScroll, "Stress Test", "Stress Test");
		
### FINAL
		''' FINISHING DRAW '''
		# Define Stack Switcher
		stackSwitcher = Gtk.StackSwitcher()
		stackSwitcher.set_stack(mainStack);
		self.vbox.pack_start(stackSwitcher, False, False, 0);
		self.vbox.pack_start(mainStack, True, True, 0);

### FUNCTIONS

### LAYER 1
	## Define the function to Change Disk Text
	def change_text_disk(self, widget, disk):
		# Get System Information, Formatted.
		partString=os.popen("lsblk -io KNAME /dev/" + disk + " | tail -n +2").read();
		partFsInfoRaw=os.popen("lsblk -io FSTYPE /dev/" + disk + " | tail -n +2").read().split("\n");
		partSizeInfo=os.popen("lsblk -io SIZE /dev/" + disk + " | tail -n +2").read();
		partMountInfoRaw=os.popen("lsblk -io MOUNTPOINT /dev/" + disk + " | tail -n +2").read().split("\n");
		typeString=os.popen("lsblk -io TYPE /dev/" + disk + " | head -n 2 | tail -n 1").read();
		hotplug=bool(int(os.popen("lsblk -io HOTPLUG /dev/" + disk + " | head -n 2 | tail -n 1").read()));
		stateString=os.popen("lsblk -io STATE /dev/" + disk + " | head -n 2 | tail -n 1").read();
		typeInt=int(os.popen("cat /sys/block/" + disk + "/queue/rotational").read());
		vendorString=os.popen("lsblk -io VENDOR /dev/" + disk + " | head -n 2 | tail -n 1").read();
		modelString=os.popen("lsblk -io MODEL /dev/" + disk + " | head -n 2 | tail -n 1").read();
		# Format System Information
		if typeInt==0:
			if hotplug==True:
				typeString="External SSD";
			else:
				typeString="Internal SSD";
		if typeInt==1:
			if typeString.rstrip()=="rom":
				typeString="ROM";
			elif typeString.rstrip()=="disk":
				if hotplug==True:
					typeString="External HD";
				else:
					typeString="Internal HDD";
			else:
				typeString="Unknown";
		if partString.strip()=="":
			partString="NONE";
			partMountInfoRaw[0]="NONE";
		else:
			for x in range(0, len(partMountInfoRaw)):
				if partMountInfoRaw[x]=='':
					partMountInfoRaw[x]="Not Mounted";
			del partMountInfoRaw[-1];
		for x in range(0, len(partFsInfoRaw)):
			if partFsInfoRaw[x]=='':
				partFsInfoRaw[x]="??";
		del partFsInfoRaw[-1];
		# Print System Information
		self.diskPartTypeLabel.set_text("TYPE:\n" + typeString);
		self.diskPartNameLabel.set_text("PARTITIONS:\nName:\n" + re.sub(' +',' ',partString.strip()));
		self.diskPartFsLabel.set_text("\nFormat:\n" + "\n".join(partFsInfoRaw));
		self.diskPartSizeLabel.set_text("\nSize:\n" + "\n".join(partSizeInfo.split()));
		self.diskPartMountLabel.set_text("\nMount point:\n" + "\n".join(partMountInfoRaw));
		self.diskVendorLabel.set_text("VENDOR:\n" + vendorString + "\nMODEL:\n" + modelString);
		self.diskStateLabel.set_text("HOTPLUGGABLE:\n" + str(hotplug) + "\n\nRUNNING:\n" + stateString);
		self.partSelectEntry.set_text("");
		self.change_part_text(self.partSelectEntry);

	## Define the function to change partition text
	def change_part_text(self, widget):
		# Sets mounted to false
		mounted=False;
		# Gets partselectstring from input
		partSelectString=self.partSelectEntry.get_text().strip();
		if os.system("lsblk /dev/" + partSelectString + " 2> /dev/null > /dev/null")==32:
			partSelectString="";
		# If partselectstring does not end with a digit, cannot be a partition.
		if partSelectString[-1:].isdigit()==False:
			partSelectString="";
		# If partselectstring is empty, act accordingly and return.
		if partSelectString=="":
			self.partSelectLabel.set_text("Enter Mounted Partition\nHere To View Details:");
			self.partDetailsLabel.set_text("Partition Details:\n");
			self.partSpaceLabel.set_text("Select Mounted Partition");
			self.partUUIDLabel.set_text("\nUUID:\nNONE");
			return;
		spaceUsedRaw=os.popen("df -h | grep /dev/" + partSelectString + " | awk '{print $5}'").read().strip().strip('%');
		# If rooted and unmounted, mount partition and set mounted to true.
		if rooted==True and spaceUsedRaw=='':
			os.system("mount /dev/" + partSelectString + " /tmp/GTKSysInfo");
			spaceUsedRaw=os.popen("df -h | grep /dev/" + partSelectString + " | awk '{print $5}'").read().strip().strip('%');
			mounted=True;
		partUUID=os.popen("lsblk -o UUID /dev/" + partSelectString + " | tail -n +2").read();
		self.partDetailsLabel.set_text("Partition Details (" + self.partSelectEntry.get_text().strip() + "):\n");
		# If could not find disk data, print messages. Else, print data.
		if spaceUsedRaw=='':
			if rooted==False:
				self.partSpaceBar.set_fraction(0);
				self.partSpaceLabel.set_text("Not a mounted partition.");
			else:
				self.partSpaceBar.set_fraction(0);
				self.partSpaceLabel.set_text("Could not mount partition.");
		else:
			spaceUsedPercent=float(spaceUsedRaw)/100;
			self.partSpaceBar.set_fraction(spaceUsedPercent);
			self.partSpaceLabel.set_text(str(int(spaceUsedPercent*100)) + "% used");
		# Print UUID.
		if partUUID.strip()=='':
			self.partUUID="\nUUID:\nNONE";
		self.partUUIDLabel.set_text("\nUUID:\n" + partUUID);
		# If mounted is true, unmount.
		if mounted==True:
			os.system("umount /tmp/GTKSysInfo");

### LAYER X
	## Stress Test Function
	def stress_test(self, widget):
		# Show spinner
		self.stressTestSpinner.start();
		# Update GUI
		self.updateGUI();
		# Get Integer Operation Data, Write to labels.
		self.intoperLabel.set_text("Integer Operations/Second (single-core): CALCULATING...\n");
		self.updateGUI();
		intoperScore=float(os.popen("./bin/c/intoper").read());
		self.intoperLabel.set_text("Integer Operations/Second (single-core): " + str(intoperScore) + " o/s\n");
		self.updateGUI();
		## Int - Multi Core
		self.intoperLabelMulti.set_text("Integer Operations/Second (multi-core): CALCULATING...\n");
		self.updateGUI();
		intoperScore=float(os.popen("./bin/c/intopermulti").read());
		self.intoperLabelMulti.set_text("Integer Operations/Second (multi-core): " + str(intoperScore) + " o/s\n");
		self.updateGUI();
		# Get Float Operation Data, Write to labels.
		self.floatoperLabel.set_text("Float Operations/Second (single-core): CALCULATING...\n");
		self.updateGUI();
		floatoperScore=float(os.popen("./bin/c/floatoper").read());
		self.floatoperLabel.set_text("Float Operations/Second (single-core): " + str(floatoperScore) + " o/s\n");
		self.updateGUI();
		## Float - Multi Core
		self.floatoperLabelMulti.set_text("Float Operations/Second (multi-core): CALCULATING...\n");
		self.updateGUI();
		floatoperScore=float(os.popen("./bin/c/floatopermulti").read());
		self.floatoperLabelMulti.set_text("Float Operations/Second (multi-core): " + str(floatoperScore) + " o/s\n");
		self.updateGUI();
		# Get Random Number Generation Data, Write to labels.
		self.randgenLabel.set_text("Random Numbers Generated/Second: CALCULATING...\n");
		self.updateGUI();
		randgenScore=float(os.popen("./bin/c/randgen").read());
		self.randgenLabel.set_text("Random Numbers Generated/Second: " + str(randgenScore) + " num/s\n");
		self.updateGUI();
		# Get RAM Speed Data, Write to labels.
		self.ramallocWriteLabel.set_text("RAM Write Speed (Bps): CALCULATING...\n");
		self.ramallocReadLabel.set_text("RAM Read Speed (Bps): CALCULATING...\n");
		self.updateGUI();
		ramallocRaw=os.popen("./bin/c/ramalloc").read().split();
		ramallocRead=ramallocRaw[1];
		ramallocWrite=ramallocRaw[0];
		self.ramallocWriteLabel.set_text("RAM Write Speed (Bps): " + ramallocWrite + " Bps\n");
		self.ramallocReadLabel.set_text("RAM Read Speed (Bps): " + ramallocRead + " Bps\n");
		self.updateGUI();
		self.stressTestSpinner.stop();

	## Stress Test Save Function
	def stress_test_save(self, widget):
		# Get Savefile
		savefiledialog = Gtk.FileChooserDialog("Save as", self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		response = savefiledialog.run();
#		# Write to file. This is a LOOONG line.
		if response == Gtk.ResponseType.OK:
			savefile = open(savefiledialog.get_filename(),'w');
			savetext = self.intoperLabel.get_text() + self.intoperLabelMulti.get_text() + self.floatoperLabel.get_text() + self.floatoperLabelMulti.get_text() + self.randgenLabel.get_text() + self.ramallocReadLabel.get_text() + self.ramallocWriteLabel.get_text();
			savefile.write(savetext);
			savefile.close();
			savefiledialog.destroy();
		else:
			savefiledialog.destroy();			

### Update GUI
	def updateGUI(self):
		for x in range(0, 10):
			time.sleep(0.1);
			Gtk.main_iteration();
		
		
# Define Exit Event
def exitevent(self, widget):
	if rooted==True:
		os.system("umount /tmp/GTKSysInfo 2> /dev/null > /dev/null");
		os.system("rmdir /tmp/GTKSysInfo");
	Gtk.main_quit();

# Start main loop
mainWin = mainClass();
mainWin.connect("delete-event", exitevent)
mainWin.show_all();
Gtk.main();

