
// Define the number of frames
 nFrames = nSlices;

// Duplicate frames using the defined range


// Creating moving average
rename("0");
run("Min...", "value=1 stack");


run("Duplicate...", "title=6 duplicate range=6-" + (nFrames - 5));
selectImage("0");
run("Duplicate...", "title=7 duplicate range=7-" + (nFrames - 4));
selectImage("0");
run("Duplicate...", "title=8 duplicate range=8-" + (nFrames - 3));
selectImage("0");
run("Duplicate...", "title=9 duplicate range=9-" + (nFrames - 2));
selectImage("0");
run("Duplicate...", "title=10 duplicate range=10-" + (nFrames - 1));
// (*note that 10-119 created a 110 frame timelapse for 11-140)
selectImage("0");
run("Merge Channels...", "c1=6 c2=7 c3=8 c4=9 c5=10 create");
rename("6-10-1");
selectImage("6-10-1");
run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");
selectImage("6-10-1");
run("Grays");



/////////////////////////////////////////////////done	now 5F versions

selectImage("6-10-1");
run("Z Project...", "projection=[Average Intensity] all");
rename("Moving Average");
run("Z Project...", "projection=[Average Intensity] all");
rename("Z proj average 6-140");
selectImage("6-10-1");
close();
run("Collect Garbage");	
selectImage("0");
run("Duplicate...", "duplicate range=11-" + nFrames);
rename("00");
selectWindow("0");
close();
// 																										

imageCalculator("Subtract create stack", "00","Moving Average");
selectWindow("Result of 00");
rename("df");
selectWindow("00");
close();
// df/f for binarised detection points to be narrowed


imageCalculator("Divide create 32-bit stack", "df","Z proj average 6-140");
selectImage("Result of df");

rename("df.f 5f-projZav.tif");
selectImage("Z proj average 6-140");
close();
selectImage("df");
close();										
selectImage("Moving Average");
close();

//////////////////																			part 2...............................................................


//5f move/proj 0.1 

selectImage("df.f 5f-projZav.tif");
run("Duplicate...", "duplicate");
selectImage("df.f 5f-projZav.tif");
rename("123");

run("Subtract...", "value=0.1 stack");/////////////////////// xxxxxxxxxx
setOption("ScaleConversions", true);
run("16-bit");
run("Multiply...", "value=10000.000 stack");
setOption("BlackBackground", true);
run("Convert to Mask", "method=Triangle background=Dark calculate black create");
selectImage("123");
close();
selectImage("MASK_123");// if i do anything else the mask just gets spottier

run("Options...", "iterations=1 count=1 black do=Open stack");
run("Options...", "iterations=1 count=1 black do=Close stack");
run("Options...", "iterations=1 count=1 black do=Dilate stack");/// new /////////////
run("Options...", "iterations=2 count=1 black do=Close stack");/// new ////////////
rename("Events binned");



//////////////////starting new FAQuA part 2



selectImage("df.f 5f-projZav-1.tif");
rename("df/f0");
selectImage("Events binned");
run("32-bit");
imageCalculator("Subtract create 32-bit stack", "df/f0","Events binned");
selectImage("Result of df/f0");
run("Min...", "value=0 stack");
rename("df/f0 without spots");
imageCalculator("Subtract create 32-bit stack", "df/f0","df/f0 without spots");
selectImage("Result of df/f0");
rename("df/f0 of hotspots*");/// made
selectImage("Events binned");
close();
selectImage("df/f0 without spots");
close();
run("Collect Garbage");	


//do trackmate and save all pots and Dialog.create("Find Maxima");

  selectImage("df/f0 of hotspots*");
 
 run("Duplicate...", "duplicate");
selectImage("df/f0 of hotspots*-1");
run("Gaussian Blur...", "sigma=1 stack");//	NEW	/////////////////////
selectImage("df/f0 of hotspots*-1"); /// start 1 get centre of hotspots* !!!
tolerance = 0.1;
type = "Single Points";
exclude = false;
light = false;

setBatchMode(true);
input = getImageID();
n = nSlices();
for (i = 1; i <= n; i++) {
    showProgress(i, n);
    selectImage(input);
    setSlice(i);
    options = "noise=" + tolerance + " output=[" + type + "]";
    if (exclude) options += " exclude";
    if (light) options += " light";
    run("Find Maxima...", options);
    if (i == 1)
        output = getImageID();
    else if (type != "Count") {
        run("Select All");
        run("Copy");
        close();
        selectImage(output);
        run("Add Slice");
        run("Paste");
    }
}
run("Select None");
setBatchMode(false);

rename("df/f0 of hotspots* Maxima1"); /// end1
selectImage("df/f0 of hotspots*-1");
close();
run("Collect Garbage");	
selectImage("df/f0 of hotspots* Maxima1");

run("Options...", "iterations=4 count=1 black do=Dilate stack"); //// initial dilation to 7X7
run("Options...", "iterations=1 count=1 black do=Close stack");// helps close adjacent 7X7

selectImage("df/f0 of hotspots* Maxima1"); /// start 2 centre of 5x5 mask of hotspots which may by 2 parts stucks !!! !!!
tolerance = 0.2;
type = "Single Points";
exclude = false;
light = false;

setBatchMode(true);
input = getImageID();
n = nSlices();
for (i = 1; i <= n; i++) {
    showProgress(i, n);
    selectImage(input);
    setSlice(i);
    options = "noise=" + tolerance + " output=[" + type + "]";
    if (exclude) options += " exclude";
    if (light) options += " light";
    run("Find Maxima...", options);
    if (i == 1)
        output = getImageID();
    else if (type != "Count") {
        run("Select All");
        run("Copy");
        close();
        selectImage(output);
        run("Add Slice");
        run("Paste");
    }
}
run("Select None");
setBatchMode(false);

rename("df/f0 of hotspots* Maxima"); /// end2

selectImage("df/f0 of hotspots* Maxima1");//delete first one
close();

selectImage("df/f0 of hotspots* Maxima");

run("Options...", "iterations=2 count=1 black do=Dilate stack"); //// second dilation to 5x5
run("Median...", "radius=1 stack");



// edits to circle?
run("32-bit");//good



selectImage("df/f0");
run("Duplicate...", "title=df/f1 duplicate");
run("Add...", "value=0.0001 stack");
imageCalculator("Subtract create 32-bit stack", "df/f1","df/f0 of hotspots* Maxima");
selectImage("Result of df/f1");
rename("Result of df/f1 holes");
run("Min...", "value=0 stack");
imageCalculator("Subtract create 32-bit stack", "df/f1","Result of df/f1 holes");
selectImage("Result of df/f1 holes");
close();
selectImage("df/f0 of hotspots* Maxima");
close();
selectImage("df/f1");
close();
selectImage("Result of df/f1");
rename("df/f0 5x5");
///////////////////made 5x5 df/f
run("Collect Garbage");	///////////////////////////////////////////////////// CG
// keep?






