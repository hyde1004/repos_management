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

    # IP
    ('syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg', 'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg'),
    ('syna-release/drm/pr_syna_ca', 'android/syna-release/drm/pr_syna_ca/root'),
    ('syna-release/drm/pr_syna_ca/3x', 'android/syna-release/drm/pr_syna_ca/3x'),
    ('syna-release/ampsdk/drm/widevine', 'android/syna-release/ampsdk/drm/widevine'),
    ('syna-release/fw_enc/mp3', 'android/syna-release/fw_enc/mp3'),
    ('syna-release/fw_enc/ms11', 'android/syna-release/fw_enc/ms11'),
    ('syna-release/ta_enc/pr32', 'android/syna-release/ta_enc/pr32'),
    ('syna-release/ta_enc/wv15', 'android/syna-release/ta_enc/wv15'),
    ('syna-release/ta_enc/libwatermark.ta', 'android/syna-release/ta_enc/libwatermark.ta'),
    ('syna-release/ta_enc/libutctl.ta', 'android/syna-release/ta_enc/libutctl.ta'),
    ('android/vendor/synaptics/playready', 'android/aosp_mirror/platform/vendor/synaptics/playready'),
    ('android/vendor/synaptics/widevine', 'android/aosp_mirror/platform/vendor/synaptics/widevine'),

    # OT
    ('android/device/synaptics/amber', 'android/aosp_mirror/device/synaptics/amber'),
    ('android/device/synaptics/amber-kernel', 'android/aosp_mirror/device/synaptics/amber-kernel'),
    ('android/vendor/synaptics/amber', 'android/aosp_mirror/platform/vendor/synaptics/amber'),
    ('syna-release/cust/amber', 'android/syna-release/cust/amber'),
]


try:
    for (syn_path, tch_repo) in repo_names:
        print('##### repo name : %s' % (syn_path))

        root_pwd = os.getcwd()
        os.chdir(syn_path)

    #    cmd = 'git remote add gitolite git@gitolite.bundang.ap.thmulti.com:/' + tch_repo +'.git'
    #    print('cmd: %s' % cmd)
        #subprocess.check_call(cmd.split(' ')) # Need to Check result
    #    subprocess.call(cmd.split(' ')) # Don't need to check result

        cmd = 'git checkout amber/bg5ct/AndroidQ/20200224/20200224/SDK'
        print('cmd: %s' % cmd)
        subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call(cmd.split(' ')) # Don't need to check result 

        cmd = 'git push gitolite amber/bg5ct/AndroidQ/20200224/20200224/SDK:tch/synaptics-sdk/amber_bg5ct_AndroidQ_20200224_20200224_SDK' # option : --dry-run
        print('cmd: %s' % cmd)
        subprocess.check_call(cmd.split(' ')) # Need to Check result
        #subprocess.call(cmd.split(' ')) # Don't need to check result 

        cmd = 'git push gitolite amber_bg5ct_AndroidQ_20200224_SDK_Release' # option : --dry-run 
        print('cmd: %s' % cmd)
        subprocess.check_call(cmd.split(' ')) # Need to Check result
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

