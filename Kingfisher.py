#!/usr/bin/python
# -*- encoding: utf-8  -*_
import os
import re
import fileinput
import sys

# filePath = "/Users/damon/Documents/work/program/iOS/sunland/sdjgactivityoperationproject"

# filePath = "/Users/damon/Documents/work/program/iOS/sunland/sdjgmessageproject"

# filePath = "/Users/damon/Documents/work/program/iOS/sunland/sdjgcommunityproject"

filePath = sys.argv[1]

allFilePathAry = []

def allFilePath( path ):
	for dirs in os.listdir(path):
		if dirs == "Pods"\
		or dirs == ".git"\
		or dirs == ".DS_Store"\
		or dirs == ".gitignore"\
		or dirs == ".podfile.swp"\
		or dirs == ".swift-version"\
		or dirs == "Podfile"\
		or dirs == "Podfile.lock"\
		or dirs == "framework"\
		or dirs == "version"\
		or dirs == "Version"\
		or dirs == "resources"\
		or dirs.endswith(".json")\
		or dirs.endswith(".h")\
		or dirs.endswith(".podspec")\
		or dirs.endswith("License")\
		or dirs.endswith("plist")\
		or dirs.endswith(".xcworkspace")\
		or dirs.endswith(".xcodeproj")\
		or dirs.endswith("UITests")\
		or dirs.endswith(".xcassets")\
		or dirs.endswith(".lproj")\
		or dirs.endswith(".xcassets")\
		or dirs.endswith(".html"):
			pass
		else:
			nextPath = path+'/'+dirs
			if os.path.isfile(nextPath):
				allFilePathAry.append(nextPath)
			else:
				allFilePath(nextPath)


def showAllPath():
	for path in allFilePathAry:
		print path	

def handleText(text):
	if "sd_setImage" in text: 
		text = re.sub("sd_setImage","kf.setImage",text)
		text = re.sub("placeholderImage","placeholder",text)
		text = re.sub("completed","completionHandler",text)
		text = re.sub("SDImageCacheType","CacheType",text)
		if "SDWebImageOptions.cacheMemoryOnly" in text:
			text = re.sub("SDWebImageOptions.cacheMemoryOnly","[.cacheMemoryOnly]",text)
		else:
			text = re.sub(".cacheMemoryOnly","[.cacheMemoryOnly]",text)
		if "SDWebImageOptions.retryFailed" in text:
			text = re.sub(", options:  SDWebImageOptions.retryFailed","",text)
			text = re.sub(", options: SDWebImageOptions.retryFailed","",text)
			text = re.sub(",options: SDWebImageOptions.retryFailed","",text)
			text = re.sub(", options:SDWebImageOptions.retryFailed","",text)
			text = re.sub(",options:SDWebImageOptions.retryFailed","",text)
		else:
			text = re.sub(", options: .retryFailed","",text)
			text = re.sub(",options: .retryFailed","",text)
			text = re.sub(", options:.retryFailed","",text)
			text = re.sub(",options:.retryFailed","",text)
		if "SDWebImageOptions.refreshCached" in text:
			text = re.sub("SDWebImageOptions.refreshCached","[.forceRefresh]",text)
		else:
			text = re.sub(".refreshCached","[.forceRefresh]",text)
	print text.rstrip("\n")

def addImport(path):
	lines = fileinput.input(path,inplace=True)
	for line in lines:
		if "import UIKit" in line:
			line = line + "import Kingfisher"
		print line.rstrip("\n")
	# lines.close()
	
def everyFile(path):
	lines = fileinput.input(path,inplace=True)
	used = False
	for line in lines:
		if "sd_setImage" in line:
			handleText(line)
			used = True
		else:
			print line.rstrip("\n")
	return used

def handleEveryFile():
	for path in allFilePathAry:
		used = everyFile(path)
		if used :
			addImport(path)



def main():
	allFilePath(filePath)
	# showAllPath()
	handleEveryFile()

if __name__ == '__main__':
    main()