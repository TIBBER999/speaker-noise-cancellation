clear 
% Directory containing WAV files
recording_wavDir = 'recording_pre_filter';  % Replace with your directory path
original_wavDir = 'soundfiles_wav';
filtered_wavDir = 'filtered_wav';

% Get a list of all WAV files in the directory
wavFiles = dir(fullfile(recording_wavDir, '*.wav'));

% Check if there are any WAV files in the directory
if isempty(wavFiles)
    error('No WAV files found in the recording directory.');
end

% Create a figure for visualization
figure;

% Loop through each WAV file
for k = 1:1
    % Get the full path of the WAV file
    filePath = fullfile(recording_wavDir, wavFiles(k).name);
    
    % Load the WAV file
    [data, fs] = audioread(filePath);
    time = (0:length(data)-1) / fs;
    
    % Create a new subplot for each WAV file
    
    subplot(numel(wavFiles), 1, k);
    plot(time, data);
    title(['WAV file: ', wavFiles(k).name]);
    xlabel('Time (s)');
    ylabel('Amplitude');
    grid on;
    xlim([0 5]); % Set x-axis limit to 10 seconds
    ylim([-1 1])
end

linkaxes(findobj(gcf, 'type', 'axes'), 'x');


% Get a list of all WAV files in the directory
OriwavFiles = dir(fullfile(recording_wavDir, '*.wav'));

% Check if there are any WAV files in the directory
if isempty(OriwavFiles)
    error('No WAV files found in the original directory.');
end

% Create a figure for visualization
figure;

% Loop through each WAV file
for k = 1:1
    % Get the full path of the WAV file
    filePath = fullfile(original_wavDir, OriwavFiles(k).name);
    
    % Load the WAV file
    [data, fs] = audioread(filePath);
    time = (0:length(data)-1) / fs;
    
    % Create a new subplot for each WAV file 
    
    subplot(numel(OriwavFiles), 1, k);
    plot(time, data);
    title(['OriWAV file: ', OriwavFiles(k).name]);
    xlabel('Time (s)');
    ylabel('Amplitude');
    grid on; 
    xlim([0 5]); % Set x-axis limit to 10 seconds
    ylim([-1 1])
end

% Synchronize the x-axes limits for better comparison
linkaxes(findobj(gcf, 'type', 'axes'), 'x');

% Print a message indicating that the plots were created
disp('All WAV files compared and visualized.');

for k = 1:numel(wavFiles)
    % Get the full path of the WAV file
    RecfilePath = fullfile(recording_wavDir, wavFiles(k).name);
    
    % Load the WAV file
    [Recdata, Recfs] = audioread(RecfilePath);
    Rectime = (0:length(Recdata)-1) / Recfs;

    OrifilePath = fullfile(original_wavDir, OriwavFiles(k).name);
    
    % Load the WAV file
    [Oridata, Orifs] = audioread(OrifilePath);
    Oritime = (0:length(Oridata)-1) / Orifs;
    
    Oridata_10 = Oridata(1:(Recfs*10), 1:2);
    %peaksnr(k) = psnr(Recdata, Oridata)
    
    X = ["Rec max", max(Recdata ), "Rec mean", mean(Recdata)];

    disp(X)
    X = ["Ori max", max(Oridata_10), "Ori mean", mean(Oridata_10)];
    disp(X)
    X =["this is for file", OrifilePath, RecfilePath];
    disp(X)

    RecMax = max(Recdata);
    RecMean = mean(Recdata);
    RecRMS = rms(Recdata);
    OriMax = max(Oridata);
    OriMean = mean(Oridata);
    OriRMS = rms(Oridata);

    MeanRatio = OriRMS/RecRMS

    Recdata = Recdata*MeanRatio;
    Fildata = Recdata - Oridata_10;

    test1data = Recdata*0 +1;
    test05data = Recdata*0 +0.5;

    audiowrite('1testdata.wav', test1data, Recfs)
    audiowrite('0.5test.wav', test05data, Recfs)

    audiowrite('Filtest.wav', Fildata, Recfs)
    audiowrite('Oritest.wav', Oridata_10, Recfs)
    audiowrite('Rectest.wav', Recdata, Recfs)

     
end
