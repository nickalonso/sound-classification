class WavFileHelper():
  
    def read_file_properties(self, filename):
    
       '''This function opens a wav file and extracts the number of speakers - 
        mono or stereo, the sample rate and the bit depth'''
        
        wave_file = open(filename, "rb")
        riff = wave_file.read(12)
        fmt = wave_file.read(36)
        
        # Extract num_channels
        num_channels_string = fmt[10:12]
        num_channels = struct.unpack('<H', num_channels_string)[0]
        
        # Extract sample_rate
        sample_rate_string = fmt[12:16]
        sample_rate = struct.unpack("<I", sample_rate_string)[0]
        
        # Extract bit_depth
        bit_depth_string = fmt[22:24]
        bit_depth = struct.unpack("<H", bit_depth_string)[0]

        return (num_channels, sample_rate, bit_depth)
       
audiodata = []
wavfilehelper = WavFileHelper()
fulldatasetpath = './UrbanSound8k'

# Etract the meta data
for index, row in metadata.iterrows():
    file_name = os.path.join(os.path.abspath(fulldatasetpath),
          'audio', 'fold' + str(row["fold"]) + '/', str(row["slice_file_name"]))                         
    data = wavfilehelper.read_file_properties(file_name)
    audiodata.append(data)
    
# Convert to Pandas dataframe
audiodf = pd.DataFrame(audiodata, columns=['num_channels','sample_rate','bit_depth'])
