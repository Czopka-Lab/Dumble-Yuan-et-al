roiManager("reset");
open("C:/x/Results/TrackRoiSet.zip");
open("C:/x/Results/ThresholdBlipRoiSet.zip");


roiManager("select all");
RoiManager.translate(0.5, 0.5);
RoiManager.scale(1.8, 1.8, true);

n = roiManager("count");
for (i = n - 1; i >= 0; i--) {
    roiManager("select", i);
    
    // Get bounds of the current ROI
    getSelectionBounds(x, y, w, h);

    // Delete ROIs touching the edges
    if (x <= 0 || y <= 0 || x + w >= getWidth || y + h >= getHeight) {
        roiManager("delete");
    } else {
        // Center coordinates of the current ROI
        centerX = x + w / 2;
        centerY = y + h / 2;

        // Create an oval ROI with height and width 9 centered at the same location
        makeOval(centerX - 5.5, centerY - 5.5, 11, 11); // Adjust for 9x9 size
        roiManager("update");
    }
}

roiManager("select all");
roiManager("Save", "C:/x/Results/FinalRoiSet.zip");

roiManager("select all");
roiManager("Multi Measure");
saveAs("Results", "C:/x/Results/RAW_Results.csv");



