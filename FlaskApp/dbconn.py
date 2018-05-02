import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost", user = "root", passwd = "Shanghai1234", db = "webdb")
	c = conn.cursor()

	return c, conn