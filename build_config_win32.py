#!python
import os
import os.path
import sys

win_def =''
arch_suffix = ''
linkflags = ''
ccflags = ''
cxxflags = ''
lib_path = [
    '#third_party/lib/eay',
]

def get_vars(isX86, msvc12):
  msvc_version = '14'
  print "Settings windows vars"
  if isX86:
    target_arch = "x86"
    arch_suffix = ''
    win_def = 'WIN32'
  else:
    target_arch = "amd64"
    arch_suffix = '_64'
    win_def = 'WIN64'
  if msvc12:
      msvc_version = '12'
  return (arch_suffix, target_arch, win_def, msvc_version)

def get_flags_win32(isRelease):
  print "get flags win32"
  ccflags = ' -nologo -Zc:wchar_t -FS -Zc:strictStrings -W3 -w44456 -w44457 -w44458 \
      -DUNICODE -D' + win_def
  cxxflags = '-nologo -Zc:wchar_t -FS -Zc:strictStrings -Zc:throwingNew -W3 -w34100 -w34189 -w44996 -w44456 -w44457 -w44458 -wd4577 -GR -EHsc \
      -DUNICODE -D' + win_def
  if isRelease:
    linkflags = '/NOLOGO /DYNAMICBASE /NXCOMPAT /INCREMENTAL:NO /SUBSYSTEM:CONSOLE'
    ccflags += ' -c -O2 -MD'
    cxxflags += ' -c -O2 -MD'
  else:
    linkflags = '/NOLOGO /DEBUG'
    ccflags += ' -c -Zi -MDd'
    cxxflags += ' -c -Zi -MDd' 
  return (ccflags, cxxflags, linkflags)

def get_qtvars(msvc_path):
  print "windows get qtvars"
  qt_dir = 'C:/Qt/5.7/' + msvc_path
  qt_include_search_path = [
      qt_dir + '/mkspecs/win32-msvc2015',
  ]
  return (qt_dir, qt_include_search_path)

