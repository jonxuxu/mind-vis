import os
import numpy as np


class Config_MBM_fMRI:
    # configs for fmri_pretrain.py
    def __init__(self):
    # --------------------------------------------
    # MAE for fMRI
        # Training Parameters
        self.lr = 2.5e-4
        self.min_lr = 0.
        self.weight_decay = 0.05
        self.num_epoch = 5
        self.warmup_epochs = 40
        self.batch_size = 100
        self.clip_grad = 0.8
        
        # Model Parameters
        self.mask_ratio = 0.75
        self.patch_size = 16
        self.embed_dim = 1024 # has to be a multiple of num_heads
        self.decoder_embed_dim = 512
        self.depth = 24
        self.num_heads = 16
        self.decoder_num_heads = 16
        self.mlp_ratio = 1.0

        # Project setting
        self.root_path = '/home/zijiao/Desktop/Zijiao/side_project/mindvis/mind-vis'
        self.output_path = self.root_path
        self.seed = 2022
        self.roi = 'VC'
        self.aug_times = 1
        self.num_sub_limit = None
        self.include_hcp = True
        self.include_kam = True
        self.accum_iter = 1

        self.use_nature_img_loss = False
        self.img_recon_weight = 0.5
        self.focus_range = None # [0, 1500] # None to disable it
        self.focus_rate = 0.6

        # distributed training
        self.local_rank = 0

class Config_MBM_finetune:
    def __init__(self):
        
        # Project setting
        self.root_path = '/home/zijiao/Desktop/Zijiao/side_project/mindvis/mind-vis'
        self.output_path = self.root_path
        self.pretrain_mae_path = os.path.join(self.root_path, 'results/fmri_pretrain/checkpoints/checkpoint.pth') 
        self.kam_path = os.path.join(self.root_path, 'data/Kamitani/npz')
        self.bold5000_path = os.path.join(self.root_path, 'data/BOLD5000')
        self.dataset = 'Kamitani_2017' # Kamitani_2017  or BOLD5000
        self.include_nonavg_test = True
        self.kam_subs = ['sbj_3']
        self.bold5000_subs = ['CSI4']

        # Training Parameters
        self.lr = 5.3e-5
        self.weight_decay = 0.05
        self.num_epoch = 15
        self.batch_size = 16 if self.dataset == 'Kamitani_2017' else 4 
        self.mask_ratio = 0.75 
        self.accum_iter = 1
        self.clip_grad = 0.8
        self.warmup_epochs = 2
        self.min_lr = 0.

        # distributed training
        self.local_rank = 0
        
class Config_Generative_Model:
    def __init__(self):
        # project parameters
        self.seed = 2022
        self.root_path = '/home/zijiao/Desktop/Zijiao/side_project/mindvis/mind-vis'
        self.kam_path = os.path.join(self.root_path, 'data/Kamitani/npz')
        self.bold5000_path = os.path.join(self.root_path, 'data/BOLD5000')
        self.roi = 'VC'
        self.patch_size = 16

        self.pretrain_mbm_path = os.path.join(self.root_path, 'pretrains/mbm/checkpoint_tuned.pth') 

        ######################################################################################
        # self.pretrain_gm_path = os.path.join(self.root_path, 'pretrains/ldm/semantic')
        self.pretrain_gm_path = os.path.join(self.root_path, 'pretrains/ldm/label2img')
        # self.pretrain_gm_path = os.path.join(self.root_path, 'pretrains/ldm/text2img-large')
        # self.pretrain_gm_path = os.path.join(self.root_path, 'pretrains/ldm/layout2img')
        
        self.dataset = 'Kamitani_2017' # Kamitani_2017 or BOLD5000
        self.kam_subs = ['sbj_3']
        self.bold5000_subs = ['CSI1']

        self.img_size = 500 if self.dataset == 'Kamitani_2017' else 256

        np.random.seed(self.seed)
        # finetune parameters
        self.batch_size1 = 5 if self.dataset == 'Kamitani_2017' else 25
        self.lr1 = 5.3e-5
        self.num_epoch_1 = 500
        
        self.precision = 32
        self.accumulate_grad = 1
        self.crop_ratio = 0.2
        self.global_pool = False
        self.use_time_cond = True
        self.eval_avg = True

        # diffusion sampling parameters
        self.num_samples = 5
        self.ddim_steps = 250
        self.HW = None
        # resume check util
        self.model_meta = None
        self.checkpoint_path = None # os.path.join(self.root_path, 'results/generation/25-08-2022-08:02:55/checkpoint.pth')
        