function OPC_calciumAnalysis ( Hz )

% script that analyses ROIs for single channel across different ROIs

% choose folder where data is stored
myFolder = '2.temp excel data';


% load matrices from excel data corresponding to fluorescence data
fPattern = fullfile( myFolder, '*transients.xlsx' );
files_trans = dir( fPattern );

% for dir to work, need to be on the MATLAB folder as current folder

for fileNo = 1:length( files_trans )
    ROIdata_All{fileNo} = xlsread( files_trans(fileNo).name );
end

% open for loop so that each timelapse/fish is done individually
for h = 1:length( ROIdata_All )

    % firstly clear repeated variables just in case

    ROI_fluoData = [];
    ROI_fluoDataTime = [];
    width_transients = [];
    amplitude_transients = [];
    eventNo_transients = [];
    widthAll = [];
    amplitudeAll = [];
    eventNoAll = [];
    amp = [];
    width = [];

    % load data for new ROI
    ROI_fluoDataTime = ROIdata_All{h};

    % convert timepoints (as frames - in first colum) to time in sec
    time = ( ROI_fluoDataTime( :,1 ) ./ Hz ) / 60;
    ROI_fluoData = ROI_fluoDataTime( :,2:end );

    % Concentrating analysis on single ROI (each column)
    for ROIno = 1:size( ROI_fluoData,2 )

        ROIno_fluoData_ROI =  [];
        ROIno_fluoData_ROI = ROI_fluoData(:,ROIno);
        norm_dFoverF = [];
        dF_overF = [];

        % Getting dF/F of for each timepoint

        % setting size of moving window to calculate baseline
        % fluorescence
        window = 4;

        for t_one = 1:size( ROI_fluoData,1 )

            % Calculating F0 as the minimum value from the previous n
            % timepoints in the trace

            if t_one <= window
                fZero = min(ROIno_fluoData_ROI(1:t_one));
            else
                fZero = min(ROIno_fluoData_ROI(t_one-window:t_one-1));
                deltaF = ROIno_fluoData_ROI(t_one) - fZero;
                dF_overF(t_one,ROIno) = deltaF./fZero;
                if isinf(dF_overF(t_one,ROIno)) == 1
                    dF_overF(t_one,ROIno) = 0;
                end
            end

        end

        % % Plot (not normalised) dF/F traces in the same figure
        % figure(1)
        % title(files_trans(h).name)
        % subplot(size( ROI_fluoData,2 ),1,ROIno)
        % hold on
        % plot( time, dF_overF(:,ROIno),'black')
        % %'-o','Color','black','MarkerSize',5, 'MarkerFaceColor','black')
        % axis padded
        % ylim([-0.1 1])
        % hold off

        % set threshold for OPC calcium event detection
        threshold_OPC = max(4.*std(dF_overF(:,ROIno)),0.1);
        
        % isolating the peaks of OPC activity and extracting their
        % amplitude and duration (half-width)
        [amp, ~, width, ~] = findpeaks(dF_overF(:,ROIno),time,'MinPeakDistance',0.05,'MinPeakHeight', threshold_OPC);
        
        % Save amplitude, duration and number of events per ROI
        widthAll{ROIno} = width.*60;
        amplitudeAll{ROIno} = amp.*100;
        eventNoAll{ROIno} = length(amp);

    end

    %% Calculations across ROIs from the same timelapse

    % Congregate all event amplitudes and widths from same fish into the same cell
    width_transients{h} = vertcat(widthAll{:});
    amplitude_transients{h} = vertcat(amplitudeAll{:});
    eventNo_transients{h} = vertcat(eventNoAll{:});

    width_fileName = ['WIDTH ' files_trans(h).name(1:end-16) '.xlsx'];
    amp_fileName = ['AMP ' files_trans(h).name(1:end-16) '.xlsx'];
    eventNo_fileName = ['FREQ ' files_trans(h).name(1:end-16) '.xlsx'];

    % Export matrices showing event amplitue, duration and frequency in
    % each timelapse as excel file
    writematrix(width_transients{h},fullfile(myFolder,width_fileName));
    writematrix(amplitude_transients{h},fullfile(myFolder,amp_fileName));
    writematrix(eventNo_transients{h},fullfile(myFolder,eventNo_fileName));

end
    

end


