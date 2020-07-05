import os
import subprocess

repo_names = [
	# syna path, tch repo name
    # common
    ('syna-release', 'android/syna-release/root'),
    ('syna-release/application', 'android/syna-release/application'),
    ('syna-release/boot', 'android/syna-release/boot/root'),
    ('syna-release/boot/preboot/prebuilts', 'android/syna-release/boot/preboot/prebuilts'),
    ('syna-release/build', 'android/syna-release/build'),
    ('syna-release/configs', 'android/syna-release/configs'),
    ('syna-release/drm', 'android/syna-release/drm/root'),
    ('syna-release/external', 'android/syna-release/external'),
    ('syna-release/factory', 'android/syna-release/factory'),
    ('syna-release/linux_4_9_q', 'android/syna-release/linux_4_9_q'),
    ('syna-release/security', 'android/syna-release/security'),
    ('syna-release/sysroot/android', 'android/syna-release/sysroot/android'),
    ('syna-release/sysroot/linux-gtb', 'android/syna-release/sysroot/linux-gtb'),
    ('syna-release/sysroot/linux-yocto', 'android/syna-release/sysroot/linux-yocto'),
    ('syna-release/sysroot/linux-yocto-72', 'android/syna-release/sysroot/linux-yocto-72'),
    ('syna-release/sysroot/linux-rootfs', 'android/syna-release/sysroot/linux-rootfs'),
    ('syna-release/ta_app', 'android/syna-release/ta_app'),
    ('syna-release/tee', 'android/syna-release/tee'),
    ('syna-release/toolchain', 'android/syna-release/toolchain'),
    ('syna-release/fw_enc', 'android/syna-release/fw_enc'),
    ('syna-release/ta_enc', 'android/syna-release/ta_enc/root'),
    ('syna-release/ampsdk', 'android/syna-release/ampsdk/root'),

    ('android/device/synaptics/sequoia', 'android/aosp_mirror/device/synaptics/sequoia'),
    ('android/device/synaptics/sequoia-kernel', 'android/aosp_mirror/device/synaptics/sequoia-kernel'),
    ('android/vendor/imagination', 'android/aosp_mirror/platform/vendor/imagination'),
    ('android/vendor/marvell', 'android/aosp_mirror/platform/vendor/marvell'),
    ('android/vendor/synaptics/build', 'android/aosp_mirror/platform/vendor/synaptics/build'),
    ('android/vendor/synaptics/common', 'android/aosp_mirror/platform/vendor/synaptics/common'),
    ('android/vendor/synaptics/overlays', 'android/aosp_mirror/platform/vendor/synaptics/overlays'),
    ('android/vendor/synaptics/sequoia', 'android/aosp_mirror/platform/vendor/synaptics/sequoia/root'),
    ('android/vendor/synaptics/external', 'android/aosp_mirror/platform/vendor/synaptics/external'),
    ('android/vendor/synaptics/vsxxx', 'android/aosp_mirror/platform/vendor/synaptics/vsxxx'),
    ('android/vendor/synaptics/sequoia/gtvs', 'android/aosp_mirror/platform/vendor/synaptics/sequoia/gtvs'),
    ('android/vendor/synaptics/netflix', 'android/aosp_mirror/platform/vendor/synaptics/netflix'),
	
    # IP
    ('syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg', 'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg'),
    ('syna-release/drm/pr_syna_ca', 'android/syna-release/drm/pr_syna_ca/root'),
    ('syna-release/drm/pr_syna_ca/4x', 'android/syna-release/drm/pr_syna_ca/4x'),
    ('syna-release/ampsdk/drm/widevine', 'android/syna-release/ampsdk/drm/widevine'),
    ('syna-release/fw_enc/mp3', 'android/syna-release/fw_enc/mp3'),
    ('syna-release/ta_enc/pr40', 'android/syna-release/ta_enc/pr40'),
    ('syna-release/ta_enc/wv15', 'android/syna-release/ta_enc/wv15'),
    ('syna-release/ta_enc/libutctl.ta', 'android/syna-release/ta_enc/libutctl.ta'),
    ('syna-release/ta_enc/libwatermark.ta', 'android/syna-release/ta_enc/libwatermark.ta'),
    ('android/vendor/synaptics/playready', 'android/aosp_mirror/platform/vendor/synaptics/playready'),
    ('android/vendor/synaptics/widevine', 'android/aosp_mirror/platform/vendor/synaptics/widevine'),
    ('syna-release/fw_enc/ms11', 'android/syna-release/fw_enc/ms11'),

    # OT
    ('android/device/synaptics/amber', 'android/aosp_mirror/device/synaptics/amber'),
    ('android/device/synaptics/amber-kernel', 'android/aosp_mirror/device/synaptics/amber-kernel'),
    ('android/vendor/synaptics/amber', 'android/aosp_mirror/platform/vendor/synaptics/amber'),
    ('syna-release/cust/amber', 'android/syna-release/cust/amber'),

]

LOCAL_BRANCH = 'amber/bg5ct/AndroidQ/20200623/202006201525/MDK'
#SYNA_BRANCH = 'debugithub/' + LOCAL_BRANCH
#TCH_BRANCH = 'synaptics/' + LOCAL_BRANCH
TCH_BRANCH = 'tch/synaptics-sdk/amber_bg5ct_AndroidQ_20200623_202006201525_MDK'

TAG = 'amber_bg5ct_AndroidQ_20200625_MDK_Release'
DO_DRY_RUN = False

try:
    dry_run = ' --dry-run' if DO_DRY_RUN else ''

    for (syn_path, tch_repo) in repo_names:
        index = repo_names.index((syn_path, tch_repo))
        print('##### repo name : %s [%d/%d]' % (syn_path, index + 1, len(repo_names)))

        root_pwd = os.getcwd()
        os.chdir(syn_path)

        # checkout
        cmd = "git checkout " + LOCAL_BRANCH
        print('cmd: %s' % cmd)
        subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call(cmd.split(' ')) # Don't need to check result 

        # add remote
        cmd = 'git remote add gitolite git@gitolite.bundang.ap.thmulti.com:/' + tch_repo +'.git'
        print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        subprocess.call(cmd.split(' ')) # Don't need to check result

        # push branch
        #cmd = "git push gitolite " + LOCAL_BRANCH +":" + TCH_BRANCH #+ " --dry-run" 
        cmd = "git push gitolite " + LOCAL_BRANCH + ":" + TCH_BRANCH + dry_run 
        print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        subprocess.call(cmd.split(' ')) # Don't need to check result 

        # delete branch
        #cmd = "git push gitolite " + LOCAL_BRANCH +":" + TCH_BRANCH #+ " --dry-run" 
        cmd = "git branch -d amber/bg5ct/AndroidQ/20200624/202006201525/MDK"
        print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        subprocess.call(cmd.split(' ')) # Don't need to check result 

        # delete remote branch
        #cmd = "git push gitolite " + LOCAL_BRANCH +":" + TCH_BRANCH #+ " --dry-run" 
        cmd = "git push gitolite :tch/synaptics-sdk/amber_bg5ct_AndroidQ_20200624_202006201525_MDK"
        print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        subprocess.call(cmd.split(' ')) # Don't need to check result 
        # push tag
#        cmd = "git push gitolite " + TAG + dry_run 
#        print('cmd: %s' % cmd)
#        subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call(cmd.split(' ')) # Don't need to check result 

        #cmd = 'git push gitolite amber_bg5ct_AndroidQ_20200224_SDK_Release' # option : --dry-run 
        #print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call(cmd.split(' ')) # Don't need to check result 

        #cmd = 'git push gitolite *:*'
        #print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call_check(cmd.split(' ')) # Don't need to check result

        os.chdir(root_pwd)

        print('\n')
        print('\n')
except subprocess.CalledProcessError as e:
        print(e.returncode)

