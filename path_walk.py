# script to clean .svn folder
import os, os.path
import stat

BASE_FOLDER = '/home/xxx/xxx/'

class Walker():
	def __init__(self, begin_path, rm_name):
		self.begin_path = begin_path
		self.rm_name = rm_name

	def going(self):
		os.path.walk(self.begin_path, self.visit, self.rm_name)

	def visit(self, arg, dirname, names):
		#if os.path.isabs(dirname):
		#	print 'absolute pathname: ', dirname
		for e in names:
			abs = os.path.join(dirname, e)
			if e == arg and os.path.isdir(abs):
				#print "Removing: ", abs
				self.rm_force(abs)
				#print "done"

	def rm_force(self, path):
		if os.path.lexists(path):
			#if path is readonly, should remove "readonly"
			self.un_readonly(path)
			if os.path.isfile(path):
				print 'Removing file: ', path
				os.remove(path)
			elif os.path.isdir(path):
				names = os.listdir(path)
				for name in names:
					abs = os.path.join(path, name)
					self.rm_force(abs)
				print 'Removing folder: ', path
				os.rmdir(path)
			else:
				os.unlink(path)
		else:
			print 'NOT EXISTS: ', path
	def is_readonly(self, path):
		st_mode = os.stat(path).st_mode
		#return st_mode == 33060
		return st_mode & stat.S_IWRITE != stat.S_IWRITE
		
	def un_readonly(self, path):
		st_mode = os.stat(path).st_mode
		os.chmod(path, st_mode | stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH) #146
		#os.chmod(path, 33206)


if __name__ == '__main__':
	if not os.path.isdir(BASE_FOLDER):
		print 'Not a folder: ', BASE_FOLDER
		exit
	walker = Walker(BASE_FOLDER, '.svn')
	#f = r't/t.txt'
	#print walker.is_readonly(f)
	#walker.un_readonly(f)
	#print walker.is_readonly(f)

	#walker.rm_force('C:\\TEMP\\zhouvi2')
	walker.going()



