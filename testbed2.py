#%%

import spikeinterface.full as si
import spikeinterface.extractors as se
# %%
rec, sorting = si.toy_example(num_segments=1, duration=200, seed=1, num_channels=16, num_columns=2)
rec  = rec.save(folder='toy_rec_new2')
# %%

sorting = si.run_sorter(sorter_name='kilosort4', recording=rec, output_folder='toy_sorting_kilosort4_n', docker_image='spikeinterface/kilosort4-base:4.0_cuda-12.0.0')
# %%
recording_spikeglx = se.read_spikeglx(folder_path="F:/NPX/BS055_20240429_g0",stream_id='imec0.ap')
#%%
output_folder1 = 'F:/NPX/sorted/BS055_20240429_g0'
sorting = si.run_sorter(sorter_name='kilosort4', recording=recording_spikeglx,
 output_folder=output_folder1, docker_image='spikeinterface/kilosort4-base:4.0_cuda-12.0.0')
# %%
