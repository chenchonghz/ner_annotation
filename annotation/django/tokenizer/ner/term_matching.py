# -*- coding: utf-8 -*- 
from django.conf import settings
from django.db import connection

import urllib2
import json

UMLS_LOOKUP_ALGORITHM_VERSION = 1

# param: source term in Chinese
# return: a tuple of two elements:
# 1) english translation, 
# 2) list of database search results. Each result is a tuple of three elements: CUI (concept ID), LUI (term ID), STR (term), AUI (unique ID)
def umls_lookup(src):
	en = translate(src.encode('utf-8'))
	re = mrconso_lookup(en)
	return (en, re)

def umls_lookup_with_translation(en):
	re = mrconso_lookup(en)
	return (en, re)

def umls_lookup_verified_match_only(src):
	cur = connection.cursor()
	query = "select CUI, LUI, STR from boson_core_lite.mrtrans_chn where NSTR = '" + src + "'"
	cur.execute(query)
	return cur.fetchone()

def insert_umls_mapping(src, en, cui, lui):
	cur = connection.cursor()
	query = "insert into boson_core_lite.mrtrans_chn (LAT, NSTR, CUI, LUI, STR, SAB) values ('CHN', '%s', '%s', '%s', '%s', 'ANNOTATION')" % (src, cui, lui, en)
	cur.execute(query)

def delete_umls_mapping(src, en, cui, lui):
	cur = connection.cursor()
	query = "delete from boson_core_lite.mrtrans_chn where LAT = 'CHN' and NSTR = '%s' and CUI = '%s' and LUI = '%s' and STR = '%s' and SAB = 'ANNOTATION' and CHID > 14368" % (src, cui, lui, en)
	cur.execute(query)

def translate(src):
	turl = "http://openapi.baidu.com/public/2.0/bmt/translate?client_id=%s&q=%s&from=zh&to=en" % (settings.BAIDU_API_KEY, src)

	req = urllib2.Request(turl)
	con = urllib2.urlopen(req).read()

	decoded = json.loads(con)
	dst = str(decoded["trans_result"][0]["dst"])

	return dst

def mrconso_lookup(term):
	cur = connection.cursor()

	query = "select CUI, LUI, STR, AUI from boson_core_lite.mrconso where STR = '" + term + "'"

	cur.execute(query)

	re = []
	re_set = set()
	for row in cur.fetchall():
		if row[1] not in re_set:
			re.append((row[0],row[1],row[2], row[3]))
		re_set.add(row[1])
	if len(re) != 0:
		return re

	query = "select CUI, LUI, STR, AUI from boson_core_lite.mrconso where "
	words = term.split(' ')
	for word in words:
		query += "STR like '%" + word + "%' and "
	query = query[:len(query)-4]

	cur.execute(query)
	results = cur.fetchall()

	for i in xrange(len(words),11):
		for row in results:
			if len(row[2].split(' ')) == i:
				re.append((row[0],row[1],row[2], row[3]))
	return re

def mrtrans_lookup(term):
	return ''
