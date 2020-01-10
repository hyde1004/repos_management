import os
import subprocess

# this script is for CJHello_bg5ct_AndroidQ_20191204_SDK_Release and CJHello_bg5ct_AndroidQ_20191206_SDK_Release
repo_names = [
  ('android/device/synaptics/sequoia', 'android/aosp_mirror/device/synaptics/sequoia'),
  ('android/device/synaptics/sequoia-kernel', 'android/aosp_mirror/device/synaptics/sequoia-kernel'),
  ('android/vendor/imagination', 'android/aosp_mirror/platform/vendor/imagination'),
#  ('android/vendor/marvell', 'android/aosp_mirror/platform/vendor/marvell'),
  ('android/vendor/synaptics/build', 'android/aosp_mirror/platform/vendor/synaptics/build'),
  ('android/vendor/synaptics/common', 'android/aosp_mirror/platform/vendor/synaptics/common'),
  ('android/vendor/synaptics/overlays', 'android/aosp_mirror/platform/vendor/synaptics/overlays'),
  ('android/vendor/synaptics/sequoia', 'android/aosp_mirror/platform/vendor/synaptics/sequoia'),
  ('android/vendor/synaptics/external', 'android/aosp_mirror/platform/vendor/synaptics/external'),
  ('android/vendor/synaptics/vsxxx', 'android/aosp_mirror/platform/vendor/synaptics/vsxxx'),
  ('android/vendor/synaptics/sequoia/gtvs', 'android/aosp_mirror/platform/vendor/synaptics/sequoia/gtvs'),
  ('android/vendor/synaptics/playready', 'android/aosp_mirror/platform/vendor/synaptics/playready'),
  ('android/vendor/synaptics/widevine', 'android/aosp_mirror/platform/vendor/synaptics/widevine'),
  ('android/device/synaptics/CJHello', 'android/aosp_mirror/device/synaptics/CJHello'),
  ('android/device/synaptics/CJHello-kernel', 'android/aosp_mirror/device/synaptics/CJHello-kernel'),
  ('android/vendor/synaptics/CJHello', 'android/aosp_mirror/platform/vendor/synaptics/CJHello'),
  ('syna-release', 'android/syna-release/root'),
  ('syna-release/application', 'android/syna-release/application'),
  ('syna-release/boot', 'android/syna-release/boot'),
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
  ('syna-release/sysroot/linux-yocto','android/syna-release/sysroot/linux-yocto'),
  ('syna-release/sysroot/linux-yocto-72', 'android/syna-release/sysroot/linux-yocto-72'),
  ('syna-release/sysroot/linux-rootfs', 'android/syna-release/sysroot/linux-rootfs'),
  ('syna-release/ta_app', 'android/syna-release/ta_app'),
  ('syna-release/tee', 'android/syna-release/tee'),
  ('syna-release/toolchain', 'android/syna-release/toolchain'),
  ('syna-release/fw_enc', 'android/syna-release/fw_enc'),
  ('syna-release/ta_enc', 'android/syna-release/ta_enc/root'),
  ('syna-release/ampsdk', 'android/syna-release/ampsdk/root'),
  ('syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg', 'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg'),
#  ('syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_wma', 'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_wma'),
  ('syna-release/drm/pr_syna_ca', 'android/syna-release/drm/pr_syna_ca/root'),
  ('syna-release/drm/pr_syna_ca/3x', 'android/syna-release/drm/pr_syna_ca/3x'),
  ('syna-release/ampsdk/drm/widevine', 'android/syna-release/ampsdk/drm/widevine'),
  ('syna-release/fw_enc/mp3', 'android/syna-release/fw_enc/mp3'),
  ('syna-release/fw_enc/ms11', 'android/syna-release/fw_enc/ms11'),
  ('syna-release/ta_enc/pr32', 'android/syna-release/ta_enc/pr32'),
#  ('syna-release/ta_enc/wv14', 'android/syna-release/ta_enc/wv14'),
  ('syna-release/ta_enc/wv15', 'android/syna-release/ta_enc/wv15'),
  ('syna-release/ta_enc/libwatermark.ta', 'android/syna-release/ta_enc/libwatermark.ta'),
#  ('syna-release/ta_enc/libwma.ta', 'android/syna-release/ta_enc/libwma.ta'),
  ('syna-release/ta_enc/libutctl.ta', 'android/syna-release/ta_enc/libutctl.ta'),
#  ('syna-release/cust/ginkgo', 'android/syna-release/cust/ginkgo'),
  ('syna-release/cust/CJHello', 'android/syna-release/cust/CJHello'),
]

'''
repo_names = [
  ('syna-release', 'android/syna-release/root'),
]
'''

'''
    cd $SYN_PATH
#    git checkout ginkgo/bg5ct/AndroidQ/20191129/201911271003/MDK
    git remote add android-b5 git@10.17.160.87:/opt/repos/$TCH_REPO
#    git push android-b5 ginkgo/bg5ct/AndroidQ/20191129/201911271003/MDK # branch
#    git push android-b5 ginkgo_bg5ct_AndroidQ_20191129_MDK_Release      # tag

# checkout
     git checkout CJHello/bg5ct/AndroidQ/20191204/201912041420/SDK

# branches
     git push android-b5 tch/synaptics-sdk/CJHello_bg5ct_AndroidQ_20191204_201912041420_SDK
     git push android-b5 tch/synaptics-sdk/CJHello_bg5ct_AndroidQ_20191206/201912041420_SDK

# tags
     git push android-b5 CJHello_bg5ct_AndroidQ_20191204_SDK_Release
     git push android-b5 CJHello_bg5ct_AndroidQ_20191206_SDK_Release

'''
try:
        for (syn_path, tch_repo) in repo_names:
                print('##### path : %s' % (tch_repo))

                root_pwd = os.getcwd()
                os.chdir(tch_repo)

                cmd = 'git branch -m tch/synaptics-sdk/CJHello_bg5ct_AndroidQ_20191206/201912041420_SDK tch/synaptics-sdk/CJHello_bg5ct_AndroidQ_20191206_201912041420_SDK'
                print('cmd: %s\n' % cmd)
                subprocess.check_call(cmd.split(' '))

                os.chdir(root_pwd)

                print('\n')
                print('\n')
except subprocess.CalledProcessError as e:
        print(e.returncode)

