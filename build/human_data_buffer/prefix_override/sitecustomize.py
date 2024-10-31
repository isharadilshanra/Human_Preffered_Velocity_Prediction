import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ishara/fyp/Human_Preffered_Velocity_Prediction/install/human_data_buffer'
