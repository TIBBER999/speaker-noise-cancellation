% Directory containing WAV files
recording_wavDir = 'recording_pre_filter';  % Replace with your directory path
original_wavDir = 'soundfiles_wav'

% Get a list of all WAV files in the directory
wavFiles = dir(fullfile(recording_wavDir, '*.wav'));

% Check if there are any WAV files in the directory
if isempty(wavFiles)
    error('No WAV files found in the recording directory.');
end

% Create a figure for visualization
figure;

% Loop through each WAV file
for k = 1:numel(wavFiles)
    % Get the full path of the WAV file
    filePath = fullfile(wavDir, wavFiles(k).name);
    
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
for k = 1:numel(OriwavFiles)
    % Get the full path of the WAV file
    filePath = fullfile(wavDir, OriwavFiles(k).name);
    
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
end

% Synchronize the x-axes limits for better comparison
linkaxes(findobj(gcf, 'type', 'axes'), 'x');

% Print a message indicating that the plots were created
disp('All WAV files compared and visualized.');

for k = 1:numel(wavFiles)
    % Get the full path of the WAV file
    RecfilePath = fullfile(wavDir, wavFiles(k).name);
    
    % Load the WAV file
    [Recdata, Recfs] = audioread(RecfilePath);
    Rectime = (0:length(Recdata)-1) / Recfs;

    OrifilePath = fullfile(wavDir, OriwavFiles(k).name);
    
    % Load the WAV file
    [Oridata, Orifs] = audioread(OrifilePath);
    Oritime = (0:length(Oridata)-1) / Orifs;
    
    
    peaksnr(k) = psnr(Recdata, Oridata)
     
end 
    