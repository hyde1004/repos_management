import os
import subprocess

repo_names = [
  'android/syna-release/root',
  'android/syna-release/application',
  'android/syna-release/boot',
  'android/syna-release/boot/preboot/prebuilts',
  'android/syna-release/build',
  'android/syna-release/configs',
  'android/syna-release/drm/root',
  'android/syna-release/external',
  'android/syna-release/factory',
  'android/syna-release/linux_4_9_q',
  'android/syna-release/security',
  'android/syna-release/sysroot/android',
  'android/syna-release/sysroot/linux-gtb',
  'android/syna-release/sysroot/linux-yocto',
  'android/syna-release/sysroot/linux-yocto-72',
  'android/syna-release/sysroot/linux-rootfs',
  'android/syna-release/ta_app',
  'android/syna-release/tee',
  'android/syna-release/toolchain',
  'android/syna-release/fw_enc',
  'android/syna-release/ta_enc/root',
  'android/syna-release/ampsdk/root',
  'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_mpeg',
  'android/syna-release/ampsdk/amp/src/ddl/acodec/codec/codec_wma',
  'android/syna-release/drm/pr_syna_ca/root',
  'android/syna-release/drm/pr_syna_ca/3x',
  'android/syna-release/ampsdk/drm/widevine',
  'android/syna-release/fw_enc/mp3',
  'android/syna-release/fw_enc/ms11',
  'android/syna-release/ta_enc/pr32',
  'android/syna-release/ta_enc/wv14',
  'android/syna-release/ta_enc/libwatermark.ta',
  'android/syna-release/ta_enc/libwma.ta',
  'android/syna-release/ta_enc/libutctl.ta',
  'android/syna-release/cust/ginkgo',
]


'''
    mkdir -p <repo name>
    cd <repo name>
    git init --bare
    cd -
'''

try:
    for repo_name in repo_names:
        print('Making %s' % (repo_name))

        cmd = 'mkdir -p %s' % (repo_name)
        subprocess.check_call(cmd.split(' '))

        root_pwd = os.getcwd()
        os.chdir(repo_name)

        cmd = 'git init --bare'
        subprocess.check_call(cmd.split(' '))

        os.chdir(root_pwd)

        print("")

except subprocess.CalledProcessError as e:
    print(e.returncode)

