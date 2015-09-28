# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
import uuid
import string


#条目可见度
ENTRY_VISIBLE_TO_CHOICES = (
	(1, "访客"),
	(2, "正式用户"),
	(3, "管理员")
	)

PATIENT_SEX_CHOICES = (
	(1, "男"),
	(2, "女")
)


#关系（1 父母，2 配偶，3 子女，4 其它）
PATIENT_RELATIVE_CHOICES = (
	(1, "父母"),
	(2, "配偶"),
	(3, "子女"),
	(4, "其他"),
	(0, ''),
)

#在随访中（1 是，2 不是）
PATIENT_IN_CONTACT_CHOICES = (
	(1, "是"),
	(2, "不是"),
	(0, ''),
	)
	


#住院科室 （1 骨科，2 放疗科，3 肿瘤科，4 血液科）
CANCER_DEPARTMENT_CHOICES = (
	(1, "骨科"),
	(2, "放疗科"),
	(3, "肿瘤科"),
	(4, "血液科"),
)

#诊断依据（1 手术病理，2 穿刺病理，3 其它）
CANCER_DIAGNOSIS_BASIS_CHOICES = (
	(1, "手术病理"),
	(2, "穿刺病理"),
	(3, "其它"),
)

#肿瘤性质（1 原发，2 转移，3 不确定）
CANCER_PROPERTY_CHOICES = (
	(1, "原发"),
	(2, "转移"),
	(3, "不确定"),
)

#肿瘤分类（1 良性，2 恶性）
CANCER_TYPE_CHOICES = (
	(1, "良性"),
	(2, "恶性")
	)

#肿瘤复发（1 首发，2 复发）
CANCER_RECURRENCE_CHOICES = (
	(1, "首发"),
	(2, "复发")
	)

#脊柱病灶数目（1 单发，2 多发）
CANCER_FOCUS_CHOICES = (
	(1, "单发"),
	(2, "多发")
	)

#肿瘤部位（1 上颈椎，2 下颈椎，3 颈胸段，4 上胸椎，5 下胸椎，6 腰椎，7 骶尾椎）
CANCER_LOCATION_CHOICES = (
	(1, "上颈椎"),
	(2, "下颈椎"),
	(3, "颈胸段"),
	(4, "上胸椎"),
	(5, "下胸椎"),
	(6, "腰椎"),
	(7, "骶尾椎"),
)

#脊柱外骨累及（1 有，2 无）
CANCER_INFECTION_SPINAL_CHOICES = (
	(1, "有"),
	(2, "无")
	)

#原发灶外重要脏器累及（如肺、肝、脑）（1 有，2 无）
CANCER_INFECTION_ORGAN_CHOICES = (
	(1, "有"),
	(2, "无")
	)

#重要脏器累及可控制（1 是，2 否）
CANCER_INFECTION_ORGAN_CONTROLLABLE_CHOICES= (
	(1, "是"),
	(2, "否")
	)


#夜间痛（1 有，2 无）
SYMPTOM_NIGHT_PAIN_CHOICES = (
	(1, "有"),
	(2, "无"),
)

#疼痛需卧床缓解（1 是，2 否）
SYMPTOM_STAY_IN_BED_CHOICES = (
	(1, "有"),
	(2, "无"),
)

#根性疼痛（1 有，2 无）
SYMPTOM_ROOT_PAIN_CHOICES = (
	(1, "有"),
	(2, "无"),
)
#肢体麻木无力（1 有，2 无）
SYMPTOM_NUMB_CHOICES = (
	(1, "有"),
	(2, "无"),
)

#体表包块（1 有，2 无）
SYMPTOM_ENCLOSED_MASS_CHOICES = (
	(1, "有"),
	(2, "无"),
)

#小便异常（1 有，2 无）
SYMPTOM_ABNORMAL_URINE_CHOICES = (
	(1, "有"),
	(2, "无"),
)
#最重病变水平以远肌力（1 正常，2 减弱
SYMPTOM_MUSCLE_CHOICES = (
	(1, "正常"),
	(2, "减弱"),
)
#最重病变水平以远感觉（1 正常，2 减弱
SYMPTOM_FEEL_CHOICES = (
	(1, "正常"),
	(2, "减弱"),
)


#手术入路（1 后路 2 前路 3 侧前方入路 4 前后联合 5颌下入路 6经口入路 7劈下颌骨入路）
TREATMENT_APPROACH_CHOICES = (
	(1, "后路"),
	(2, "前路"),
	(3, "侧前方入路"),
	(4, "前后联合"),
	(5, "颌下入路"),
	(6, "经口入路"),
	(7, "劈下颌骨入路"),
)

#手术部位（1上颈椎 2下颈椎 3颈胸段 4上胸椎 5下胸椎 6腰椎 7骶骨）
TREATMENT_LOCATION_CHOICES = (
	(1, "上颈椎"),
	(2, "下颈椎"),
	(3, "颈胸段"),
	(4, "上胸椎"),
	(5, "下胸椎"),
	(6, "腰椎"),
	(7, "骶骨"),
)

#手术方式（1姑息性减压 2囊内刮除 3囊外经瘤切除 4边缘性整块切除 5广泛性整块切除）
TREATMENT_METHOD_CHOICES = (
	(1, "姑息性减压"),
	(2, "囊内刮除"),
	(3, "囊外经瘤切除"),
	(4, "边缘性整块切除"),
	(5, "广泛性整块切除"),
)


#术后并发症（1伤口感染 2咽后壁感染或不愈合 3肺炎 4泌尿系感染 5神经损害表现）
TREATMENT_POST_COMPLICATION_CHOICES = (
	(1, "伤口感染"),
	(2, "咽后壁感染或不愈合"),
	(3, "肺炎"),
	(4, "泌尿系感染"),
	(5, "神经损害表现"),
)

#部位（1 椎体一侧 2 整个椎体 3椎体一侧+附件 4整个椎体+附件）
TREATMENT_BONE_CEMENT_LOCATION_CHOICES = (
	(1, "椎体一侧"),
	(2, "整个椎体"),
	(3, "椎体一侧+附件"),
	(4, "整个椎体+附件"),
)

#支具类型（1 Halo架，2 枕颈胸支具，3 颈椎围领（颈托），4 胸腰椎支具）
TREATMENT_SUPPORT_THERAPY_TYPE_CHOICES = (
	(1, "Halo架"),
	(2, "枕颈胸支具"),
	(3, "颈椎围领（颈托）"),
	(4, "胸腰椎支具"),
)
#药物（1 二磷酸盐，2 狄诺塞麦，3干扰素，靶向药物） other_treatment_drug
TREATMENT_OTHER_TREATMENT_DRUG_CHOICES = (
	(1, "二磷酸盐"),
	(2, "狄诺塞麦"),
	(3, "干扰素"),
	(4, "靶向药物"),
)

#项目名称（1 手术病理， 2 穿刺病理， 3 PET-CT， 4 病变MR， 5 病变CT， 6 病变X线片 7 骨扫描）
TEST_PROJECT_NAME_CHOICES = (
	(1, "手术病理"),
	(2, "穿刺病理"),
	(3, "PET-CT"),
	(4, "病变MR"),
	(5, "病变CT"),
	(6, "病变X线片"),
	(7, "骨扫描"),
)

################################################################################

PATIENT_LABELS = {
			'title': 'Title (Experiment Name)',
			'experiment_date':'Date to run MiSeq',
			'description': 'Description (sufficient information for reviewers to understand this experiment)'#mark_safe('Description (sufficient information for this screen, (<a href="/virtual/new/example/#desc" target="_blank">Example</a>)'),
		}

class Patient(models.Model):
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)
	
	sex = models.CharField(max_length=200,blank=True, null=True) #models.IntegerField(choices=PATIENT_SEX_CHOICES, null=True,blank=True,)  TODO
	DOB = models.CharField(max_length=200,blank=True,null=True) #models.DateField(blank=True,null=True) TODO
	social_id = models.CharField(max_length=200,blank=True,null=True)
	location = models.CharField(max_length=200,blank=True,null=True)
	phone = models.CharField(max_length=200,blank=True,null=True)
	DOD = models.CharField(max_length=200,blank=True, null=True) #models.DateField(blank=True,null=True) TODO

	#INCOMPLETE FIELDS
	relative = models.IntegerField(choices=PATIENT_RELATIVE_CHOICES, blank=True,default=0)  #关系（1 父母，2 配偶，3 子女，4 其它）
	relative_phone = models.CharField(max_length=200,blank=True,null=True)
	relative_email  = models.EmailField(max_length=200,blank=True,null=True)
	relative_wechat = models.CharField(max_length=200,blank=True,null=True)
	relative_in_contact = models.IntegerField(choices = PATIENT_IN_CONTACT_CHOICES,blank=True,default=0)

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='patient_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='patient_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='patient_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))

	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID

	@property
	def get_standard_DOB_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.DOB) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.DOB

	@property
	def get_standard_DOD_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.DOD) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.DOD

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))

'''
	def natural_key(self):
			return (self.name,self.db_id)

	def get_all_samples(self):
		return self.sample_set.all()

	@property
	def get_sorted_sample_set(self):
				return self.sample_set.order_by('created_date')
	@property
	def get_standard_created_date(self):
		#return "%s-%s-%s"%(self.created_date.year, self.created_date.month, self.created_date.day )
		return datetime.datetime(self.created_date.year, self.created_date.month, self.created_date.day,self.created_date.hour,self.created_date.minute,self.created_date.second)
	@property
	def get_taged_project_name(self):
		return u"<span class=\'label label-info\' style=\'font-size:85%%;font-weight:500;background-color:#9999FF;\'><a href=\'%s\'><font color='white'>%s</font></a></span>" % ('/virtual/search/?p='+self.project_name.replace('\s+','%20'), self.project_name)

	@property
	def get_taged_investigator_name(self):
		tags = []
		for i in self.investigator.all():
			tags.append("<span class=\'label label-info\' style=\'font-size:85%%;font-weight:500;background-color:#66C285;\'><a href=\'%s\'><font color='white'>%s</font></a></span>" % ('/virtual/search/?u='+'%20'.join([i.FirstName, i.LastName]), ' '.join([i.FirstName, i.LastName])))
		
		return ', '.join(tags)

	@property
	def get_comma_separated_investigator_name(self):
				tags = []
				for i in self.investigator.all():
						tags.append(' '.join([i.FirstName, i.LastName]))

				return ', '.join(tags)
	
	@property
		def get_taged_created_by_name(self):
				if self.created_by:
			tags="<span class=\'label label-info\' style=\'font-size:85%%;font-weight:500;background-color:#66C285;\'><a href=\'%s\'><font color='white'>%s</font></a></span>" % ('/virtual/search/?u='+'%20'.join([self.created_by.FirstName, self.created_by.LastName]), ' '.join([self.created_by.FirstName, self.created_by.LastName]))

					return tags
		else:
			return ''


	@property	
	def get_absolute_url(self):
		return "/virtual/get/%s/" % self.experiment_id

'''

class Cancer(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='cancers') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)
	
	admission_date = models.CharField(max_length=200,blank=True, null=True) #models.DateField(blank=True,null=True) TODO
	discharge_date = models.CharField(max_length=200,blank=True, null=True) #models.DateField(blank=True,null=True) TODO
	department = models.IntegerField(choices=CANCER_DEPARTMENT_CHOICES, null=True,blank=True,)
	pre_diagnosis = models.CharField(max_length=200,blank=True,null=True)
	diagnosis = models.CharField(max_length=200,blank=True,null=True)
	diagnosis_basis = models.IntegerField(choices=CANCER_DIAGNOSIS_BASIS_CHOICES, null=True,blank=True,)
	cancer_property = models.IntegerField(choices=CANCER_PROPERTY_CHOICES, null=True,blank=True,)
	cancer_type = models.IntegerField(choices=CANCER_TYPE_CHOICES, null=True,blank=True,)
	recurrence = models.IntegerField(choices=CANCER_RECURRENCE_CHOICES, null=True,blank=True,)
	focus = models.IntegerField(choices=CANCER_FOCUS_CHOICES, null=True,blank=True,)
	location = models.IntegerField(choices=CANCER_LOCATION_CHOICES, null=True,blank=True,)
	infection_spinal = models.IntegerField(choices=CANCER_INFECTION_SPINAL_CHOICES, null=True,blank=True,)
	infection_organ = models.IntegerField(choices=CANCER_INFECTION_ORGAN_CHOICES, null=True,blank=True,)
	infection_organ_controllable = models.IntegerField(choices=CANCER_INFECTION_ORGAN_CONTROLLABLE_CHOICES, null=True,blank=True,)

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='cancer_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='cancer_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='cancer_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))
	
	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID
	
	@property
	def get_standard_admission_date_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.admission_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.admission_date

	@property
	def get_standard_discharge_date_date(self):
		datemode = 0
		# datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.discharge_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.discharge_date

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))


'''
	@property
	def get_treatment_dosage_display(self):
		data = ''
		if self.treatment is not None:
			data = self.treatment.compoundName
		if self.treatment_dose is not None:
			data +=	' ('+str(self.treatment_dose)+' nM)'
		return data

	@property
		def get_pool_numbers_display(self):
				if self.pool_number is not None:
						tmp=[]
			for pool in self.pool_number.all():
				tmp.append(pool.description)
			data = ','.join(tmp)
				return data


'''


class Symptom(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='symptoms') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)
	
	admission_date = models.CharField(max_length=200,blank=True, null=True) #models.DateField(blank=True,null=True) TODO
	pain_VAS = models.CharField(max_length=2, null=True,blank=True,)
	night_pain = models.IntegerField(choices=SYMPTOM_NIGHT_PAIN_CHOICES, null=True,blank=True,)
	stay_in_bed = models.IntegerField(choices=SYMPTOM_STAY_IN_BED_CHOICES, null=True,blank=True,)
	root_pain = models.IntegerField(choices=SYMPTOM_ROOT_PAIN_CHOICES, null=True,blank=True,)
	numb = models.IntegerField(choices=SYMPTOM_NUMB_CHOICES, null=True,blank=True,)
	enclosed_mass = models.IntegerField(choices=SYMPTOM_ENCLOSED_MASS_CHOICES, null=True,blank=True,)
	abnormal_urine = models.IntegerField(choices=SYMPTOM_ABNORMAL_URINE_CHOICES, null=True,blank=True,)
	duration = models.CharField(max_length=200,blank=True,null=True)
	muscle = models.IntegerField(choices=SYMPTOM_MUSCLE_CHOICES, null=True,blank=True,)
	feel = models.IntegerField(choices=SYMPTOM_FEEL_CHOICES, null=True,blank=True,)

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='symptom_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='symptom_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='symptom_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))

	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID

	@property
	def get_standard_admission_date_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.admission_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.admission_date

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))



class Treatment(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='treatments') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)

	surgery_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)
	surgeon = models.CharField(max_length=200,blank=True,null=True)  #TODO
	approach = models.IntegerField(choices=TREATMENT_APPROACH_CHOICES, null=True,blank=True,)
	location = models.IntegerField(choices=TREATMENT_LOCATION_CHOICES, null=True,blank=True,)
	method = models.IntegerField(choices=TREATMENT_METHOD_CHOICES, null=True,blank=True,)
	envelope_damage = models.IntegerField(choices=((1,"有"),(2,"无"),), null=True,blank=True,) #TREATMENT_METHOD_CHOICES
	sacrifice = models.CharField(max_length=200,blank=True,null=True) #TODO
	bone_cement = models.IntegerField(choices=((1,"有"),(2,"无"),), null=True,blank=True,) #术中骨水泥强化（1 有，2 无
	radiofrequency = models.IntegerField(choices=((1,"有"),(2,"无"),), null=True,blank=True,) 
	total_time = models.IntegerField(null=True,blank=True)
	bleeding_vol = models.IntegerField(null=True,blank=True)
	allogeneic_blood = models.IntegerField(null=True,blank=True)
	surgery_complication = models.CharField(max_length=200,blank=True,null=True) #TODO
	surgery_comment = models.CharField(max_length=200,blank=True,null=True)
	post_complication = models.IntegerField(choices=TREATMENT_POST_COMPLICATION_CHOICES, null=True,blank=True,)
	arterial_embolization_method = models.CharField(max_length=200,blank=True,null=True)  # 动脉栓塞 方式
	arterial_embolization_name = models.CharField(max_length=200,blank=True,null=True)  # 动脉栓塞 动脉名称
	bone_cement_num = models.CharField(max_length=200,blank=True,null=True)
	bone_cement_location = models.IntegerField(choices=TREATMENT_BONE_CEMENT_LOCATION_CHOICES, null=True,blank=True,)
	support_therapy_type = models.IntegerField(choices=TREATMENT_SUPPORT_THERAPY_TYPE_CHOICES, null=True,blank=True,)
	support_therapy_start_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True) TODO
	radiotherapy_dose = models.CharField(max_length=200,blank=True,null=True)
	radiotherapy_course = models.CharField(max_length=200,blank=True,null=True)
	radiotherapy_start_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)
	chemotherapy_plan = models.CharField(max_length=200,blank=True,null=True)
	chemotherapy_start_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)
	other_treatment_drug = models.IntegerField(choices=TREATMENT_OTHER_TREATMENT_DRUG_CHOICES, null=True,blank=True,)
	other_treatment_start_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)
	other_treatment_end_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='treatment_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='treatment_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='treatment_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))
	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID
	
	@property
	def get_standard_surgery_date_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.surgery_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.surgery_date

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))



class Test(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='tests') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)

	project_date = models.CharField(max_length=200,blank=True,null=True)#models.DateField(blank=True,null=True)
	project_name = models.IntegerField(choices=TEST_PROJECT_NAME_CHOICES, null=True,blank=True,)
	result_discription = models.CharField(max_length=200,blank=True,null=True)
	diagosis = models.CharField(max_length=200,blank=True,null=True)
	pre_test = models.IntegerField(choices=((1,"是"),(2,"否"),), null=True,blank=True,)
	wbb_1_12 = models.CharField(max_length=200,blank=True,null=True)
	wbb_A_F = models.CharField(max_length=200,blank=True,null=True)
	CT_property = models.IntegerField(choices=((1,"溶骨"),(2,"成骨"),(3,"混合")), null=True,blank=True,)
	X_ray = models.IntegerField(choices=((1,"正常"),(2,"半脱位/滑移"),(3,"侧凸/后凸")), null=True,blank=True,)
	collapse = models.IntegerField(choices=((1,"<50%"),(2,">50%"),(3,"受累>50%但无塌陷"),(4,"无")), null=True,blank=True,)
	lateral_involvement = models.IntegerField(choices=((1,"是"),(2,"否"),(3,"不涉及")), null=True,blank=True,)
	vertebral_artery_involvement = models.CharField(max_length=200,blank=True,null=True)
	enneking = models.CharField(max_length=200,blank=True,null=True)

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='test_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='test_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='test_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))

	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID
	
	@property
	def get_standard_project_date_date(self):
	    datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
	    try:
	    	return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.project_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
	    except ValueError:
	    	return self.project_date

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))



class FollowUp(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='followups') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)

	major_complain = models.CharField(max_length=200,blank=True,null=True)
	recurrence = models.IntegerField(choices=((1,"有"),(2,"无"),), null=True,blank=True,)
	transfer = models.IntegerField(choices=((1,"有"),(2,"无"),), null=True,blank=True,)
	fixation_loose = models.IntegerField(choices=((1,"是"),(2,"否"),), null=True,blank=True,)
	fixation_break = models.IntegerField(choices=((1,"是"),(2,"否"),), null=True,blank=True,)
	CT_fusion = models.IntegerField(choices=((1,"是"),(2,"否"),), null=True,blank=True,)
	method  = models.IntegerField(choices=((1,"病人来诊"),(2,"电话咨询"),), null=True,blank=True,)
	DOD = models.CharField(max_length=200,blank=True,null=True)  # models.DateField(blank=True,null=True) TODO
	followup_date = models.CharField(max_length=200,blank=True,null=True)  # models.DateField(blank=True,null=True) TODO

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='followup_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='followup_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='followup_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))

	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))


'''	
	@property
	def get_standard_followup_date_date(self):
	    datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
	    return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.followup_date) + 1462 * datemode)).strftime("%Y-%m-%d ")
'''


class Questionnaire(models.Model):
	patient = models.ForeignKey(Patient,null=True,blank=True,related_name='questionnarires') # models.ForeignKey(Patient, null=True,related_name='cancers') TODO
	DB_ID = models.CharField(max_length=200,blank=True) #, unique=True) TODO
	name = models.CharField(max_length=200,blank=True, null=True)
	EMR_id = models.CharField(max_length=200,blank=True,null=True)

	EQ5D_1 = models.IntegerField(null=True,blank=True)
	EQ5D_2 = models.IntegerField(null=True,blank=True)
	EQ5D_3 = models.IntegerField(null=True,blank=True)
	EQ5D_4 = models.IntegerField(null=True,blank=True)
	EQ5D_5 = models.IntegerField(null=True,blank=True)

	date = models.CharField(max_length=200,blank=True,null=True)  # models.DateField(blank=True,null=True) TODO

	#DEFAULT FIELDS
	visible_to = models.IntegerField(choices = ENTRY_VISIBLE_TO_CHOICES,blank=True,default=2)
	tagged = models.NullBooleanField(blank=True,null=True)
	comment =  models.CharField(max_length=200,blank=True,null=True)
	created_by = models.ForeignKey(User,blank=True,null=True,related_name='questionnaire_created')
	created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
	updated_by = models.ManyToManyField(User,blank=True,related_name='questionnaire_updated')
	updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
	download_by = models.ManyToManyField(User,blank=True,related_name='questionnaire_download')
	download_date = models.DateTimeField("Download Date",null=True,blank=True)

	def __unicode__(self):
		return smart_unicode('-'.join([self.DB_ID,str(self.id)]))

	@property	
	def get_absolute_url(self):
		return "/dashboard/get/%s/" % self.DB_ID

	@property
	def get_standard_date_date(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		try:
			return (datetime.datetime(1899, 12, 30) + datetime.timedelta(days=float(self.date) + 1462 * datemode)).strftime("%Y-%m-%d ")
		except ValueError:
			return self.date

	@property
	def get_standard_EMR_id(self):
		datemode = 0
	    # datemode: 0 for 1900-based, 1 for 1904-based
		return int(float(self.EMR_id))


		
class Log(models.Model):
    writer = models.ManyToManyField(User,related_name='writer',blank=True)
    subject = models.CharField(max_length=500)
    content = models.TextField()
    related_obj = models.ForeignKey(Patient,blank=True,null=True,related_name='related_log')
    visible_to =  models.CharField(blank=True,max_length=20,
                        choices = (
                        ("访客", "访客"),
                        ("正式用户", "正式用户"),
                        ("我自己", "我自己"),
                ),
                default="我自己",
        )

    created_by = models.ForeignKey(User,blank=True,null=True,related_name='log_created_by')
    created_date = models.DateTimeField("Created Date",default=datetime.datetime.now,blank=True)
    updated_by = models.ManyToManyField(User,blank=True,related_name='log_updated_by')
    updated_date = models.DateTimeField("Updated date",auto_now_add=False, auto_now=True,blank=True,null=True)
    download_by = models.ManyToManyField(User,blank=True,related_name='log_download_by')
    download_date = models.DateTimeField("Download Date",null=True,blank=True)

    def __unicode__(self):
            return unicode(self.subject)


