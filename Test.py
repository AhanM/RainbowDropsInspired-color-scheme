'''
This is about <code>ClassName</code>.
{@link com.yourcompany.aPackage.Interface}
@author Author
@deprecated use <code>OtherClass</code>.
'''
class AnyClass(AbstractClassName):
	""" This comment may span multiple lines """
	def __init__(self, arg, field):
		super(AnyClass, self).__init__()
		self.arg = arg
		self.field = field
		
	# This comment may span only this line
	def foo(parameter):
		abstractMethod(inheritedField)
		local = 42*hashCode()
		staticMethod()
		return bar(local) + parameter

	def getField():
		return field
