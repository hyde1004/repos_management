import os
import subprocess

repo_names = [
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
    ('syna-release/linux_4_14', 'android/syna-release/linux_4_14'),
    ('syna-release/security', 'android/syna-release/security'),
    ('syna-release/sysroot/android', 'android/syna-release/sysroot/android'),
    ('syna-release/sysroot/linux-gtb', 'android/syna-release/sysroot/linux-gtb'),
    ('syna-release/sysroot/linux-rootfs', 'android/syna-release/sysroot/linux-rootfs'),
    ('syna-release/ta_app', 'android/syna-release/ta_app'),
    ('syna-release/tee', 'android/syna-release/tee'),
    ('syna-release/toolchain', 'android/syna-release/toolchain'),
    ('syna-release/fw_enc', 'android/syna-release/fw_enc'),
    ('syna-release/ta_enc', 'android/syna-release/ta_enc/root'),
    ('syna-release/ampsdk', 'android/syna-release/ampsdk/root'),
    ('syna-release/osal', 'android/syna-release/osal'),
    ('android/vendor/imagination', 'android/aosp_mirror/platform/vendor/imagination'),
    ('android/vendor/marvell', 'android/aosp_mirror/platform/vendor/marvell'),
    ('android/vendor/synaptics/build', 'android/aosp_mirror/platform/vendor/synaptics/build'),
    ('android/vendor/synaptics/common', 'android/aosp_mirror/platform/vendor/synaptics/common'),
    ('android/vendor/synaptics/overlays', 'android/aosp_mirror/platform/vendor/synaptics/overlays'),
    ('android/vendor/synaptics/external', 'android/aosp_mirror/platform/vendor/synaptics/external'),
    ('android/vendor/synaptics/vsxxx', 'android/aosp_mirror/platform/vendor/synaptics/vsxxx'),
    ('android/vendor/synaptics/dolphin/gtvs', 'android/aosp_mirror/platform/vendor/synaptics/dolphin/gtvs'),
    ('android/device/synaptics/dolphin', 'android/aosp_mirror/device/synaptics/dolphin'),
    ('android/device/synaptics/dolphin-kernel', 'android/aosp_mirror/device/synaptics/dolphin-kernel'),
    ('android/vendor/synaptics/dolphin', 'android/aosp_mirror/platform/vendor/synaptics/dolphin'),
    ('android/vendor/vsi', 'android/aosp_mirror/platform/vendor/vsi'),

    # IP
    ('syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg', 'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg'),
    ('syna-release/fw_enc/mp3', 'android/syna-release/fw_enc/mp3'),
    ('syna-release/ta_enc/libwatermark.ta', 'android/syna-release/ta_enc/libwatermark.ta'),

    # OT
    ('android/device/synaptics/igarnet', 'android/aosp_mirror/device/synaptics/igarnet'),
    ('android/device/synaptics/igarnet-kernel', 'android/aosp_mirror/device/synaptics/igarnet-kernel'),
    ('android/vendor/synaptics/igarnet', 'android/aosp_mirror/platform/vendor/synaptics/igarnet'),
    ('syna-release/cust/igarnet', 'android/syna-release/cust/igarnet'),

]

LOCAL_BRANCH = 'igarnet/vs680/AndroidQ/20200515/202005111414/SDK'
#SYNA_BRANCH = 'debugithub/' + LOCAL_BRANCH
#TCH_BRANCH = 'synaptics/' + LOCAL_BRANCH
TCH_BRANCH = 'tch/synaptics-sdk/igarnet_vs680_AndroidQ_20200515_202005111414_SDK'

TAG = 'igarnet_20200515_SDK_Release'
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

        # push tag
        cmd = "git push gitolite " + TAG + dry_run 
        print('cmd: %s' % cmd)
        subprocess.check_call(cmd.split(' ')) # Need to Check result
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

