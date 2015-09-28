# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.core.mail import send_mail,mail_admins
from django.core.mail import EmailMessage,EmailMultiAlternatives

from django.template.defaulttags import register

from django.contrib.auth.decorators import login_required



from .models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire
from forms import NewPatientForm,PatientForm, CancerForm, SymptomForm, TreatmentForm, TestForm, FollowUpForm, QuestionnaireForm

import xlsxwriter
import StringIO

#PARAMETERS
DB_NAME_DISPLAY = {
	'patient':"病人基本信息",
	'cancer':"肿瘤基本信息",
	'symptom':"症状与体征",
	'treatment':"治疗情况",
	'test':"辅助检查",
	'followup':"随访情况",
	'questionnaire' : "问卷评分"
	}



def is_guest(user):
	return user.groups.filter(name='guest').exists()


@login_required
def index(request):

	if request.POST:
		if 'sendEmail' in request.POST:
			fromemail = request.user.email
			header = request.POST['subject']
			to = request.POST['emailto'].split(',')
			content = request.POST['content']
			msg = EmailMultiAlternatives(header, content, fromemail, to)
			msg.content_subtype = "html"
			msg.send()

			return HttpResponseRedirect('/dashboard/confirm/?h=success&t=Email Sent! &b1=back&b2=dashboard')

	else:
		if is_guest(request.user):
			objs = Patient.objects.filter(visible_to=1).order_by('DB_ID')
			marked = Patient.objects.filter(visible_to=1).filter(tagged=True).order_by('DB_ID')
		else:
			objs = Patient.objects.filter(visible_to=2).order_by('DB_ID')#(surgeon__iexact=u'刘忠军')#request.user.username).order_by('DB_ID')
			marked = Patient.objects.filter(visible_to=2).filter(tagged=True).order_by('DB_ID')#(surgeon__iexact=u'刘忠军')#request.user.username).order_by('DB_ID')
		args = {}
		args.update(csrf(request))
		args['user'] = request.user
		args['objs'] = objs
		args['marked'] = marked
		args['banner'] = request.GET.get('banner', '').split('_')

		return render_to_response('consoleView/account.html',args)

@login_required
def db_search(request,db_name):

	if db_name == 'patient':
		objs =  Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'cancer':
		objs =  Cancer.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'symptom':
		objs =  Symptom.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'treatment':
		objs =  Treatment.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'test':
		objs =  Test.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'followup':
		objs =  FollowUp.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	if db_name == 'questionnaire':
		objs =  Questionnaire.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')

	if is_guest(request.user):
		objs =  objs.filter(visible_to=1).order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	
	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['db_name'] = db_name
	args['db_name_ch'] = DB_NAME_DISPLAY[db_name]
	args['objs'] = objs
	args['k'] = request.GET.get('k', '')

	return render_to_response('DBView/db_search.html',args)

@login_required
def db_download(request,db_name):
	if request.POST:
		output = StringIO.StringIO()
		wb = xlsxwriter.Workbook(output, {'in_memory': True})
		ws = wb.add_worksheet()

		indexes = request.POST.getlist('indexes[]')

		if db_name == 'patient':
			all_objs = Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'性别')
			ws.write(0, 3, u'出生年月')
			ws.write(0, 4, u'身份证号')
			ws.write(0, 5, u'地区')
			ws.write(0, 6, u'随访电话')
			ws.write(0, 7, u'去世日期')
			ws.write(0, 8, u'关系')
			ws.write(0, 9, u'电话')
			ws.write(0, 10, u'Email')
			ws.write(0, 11, u'微信')
			ws.write(0, 12, u'在随访中')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.sex)
				ws.write(row_num, 3, obj.DOB)
				ws.write(row_num, 4, obj.social_id)
				ws.write(row_num, 5, obj.location)
				ws.write(row_num, 6, obj.phone)
				ws.write(row_num, 7, obj.DOD)
				ws.write(row_num, 8, (obj.get_relative_display() or ''))
				ws.write(row_num, 9, obj.relative_phone)
				ws.write(row_num, 10, obj.relative_email)
				ws.write(row_num, 11, obj.relative_wechat)
				ws.write(row_num, 12, (obj.get_relative_in_contact_display() or ''))
				row_num += 1
		if db_name == 'cancer':
			all_objs =  Cancer.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'入院日期')
			ws.write(0, 3, u'出院日期')
			ws.write(0, 4, u'住院科室')
			ws.write(0, 5, u'术前诊断')
			ws.write(0, 6, u'最终诊断')
			ws.write(0, 7, u'诊断依据')
			ws.write(0, 8, u'肿瘤性质')
			ws.write(0, 9, u'肿瘤分类')
			ws.write(0, 10, u'肿瘤复发')
			ws.write(0, 11, u'脊柱病灶数目')
			ws.write(0, 12, u'肿瘤部位')
			ws.write(0, 13, u'脊柱外骨累及')
			ws.write(0, 14, u'原发灶外重要脏器累及')
			ws.write(0, 15, u'重要脏器累及可控制')
			ws.write(0, 16, u'备注')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.admission_date)
				ws.write(row_num, 3, obj.discharge_date)
				ws.write(row_num, 4, (obj.get_department_display() or ''))
				ws.write(row_num, 5, obj.pre_diagnosis)
				ws.write(row_num, 6, obj.diagnosis)
				ws.write(row_num, 7, (obj.get_diagnosis_basis_display() or ''))
				ws.write(row_num, 8, (obj.get_cancer_property_display() or ''))
				ws.write(row_num, 9, (obj.get_cancer_type_display() or ''))
				ws.write(row_num, 10, (obj.get_recurrence_display() or ''))
				ws.write(row_num, 11, (obj.get_focus_display() or ''))
				ws.write(row_num, 12, (obj.get_location_display() or ''))
				ws.write(row_num, 13, (obj.get_infection_spinal_display() or ''))
				ws.write(row_num, 14, (obj.get_infection_organ_display() or ''))
				ws.write(row_num, 15, (obj.get_infection_organ_controllable_display() or ''))
				ws.write(row_num, 16, obj.comment)
				row_num += 1
		if db_name == 'symptom':
			all_objs =  Symptom.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'入院日期')
			ws.write(0, 3, u'疼痛VAS（轻中重）t为不清')
			ws.write(0, 4, u'夜间痛')
			ws.write(0, 5, u'疼痛需卧床缓解')
			ws.write(0, 6, u'根性疼痛')
			ws.write(0, 7, u'肢体麻木无力')
			ws.write(0, 8, u'体表包块')
			ws.write(0, 9, u'小便异常')
			ws.write(0, 10, u'病程时间（月）')
			ws.write(0, 11, u'最重病变水平以远肌力')
			ws.write(0, 12, u'最重病变水平以远感觉')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.admission_date)
				ws.write(row_num, 3, obj.pain_VAS)
				ws.write(row_num, 4, (obj.get_night_pain_display() or ''))
				ws.write(row_num, 5, (obj.get_stay_in_bed_display() or ''))
				ws.write(row_num, 6, (obj.get_root_pain_display() or ''))
				ws.write(row_num, 7, (obj.get_numb_display() or ''))
				ws.write(row_num, 8, (obj.get_enclosed_mass_display() or ''))
				ws.write(row_num, 9, (obj.get_abnormal_urine_display() or ''))
				ws.write(row_num, 10, obj.duration)
				ws.write(row_num, 11, (obj.get_muscle_display() or ''))
				ws.write(row_num, 12, (obj.get_feel_display() or ''))
				row_num += 1
		if db_name == 'treatment':
			all_objs =  Treatment.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'手术日期')
			ws.write(0, 3, u'术者')
			ws.write(0, 4, u'手术入路')
			ws.write(0, 5, u'手术部位')
			ws.write(0, 6, u'手术方式')
			ws.write(0, 7, u'肿瘤包膜破损情况')
			ws.write(0, 8, u'为保证边界牺牲的组织')
			ws.write(0, 9, u'术中骨水泥强化')
			ws.write(0, 10, u'术中射频消融')
			ws.write(0, 11, u'手术总时间（min）')
			ws.write(0, 12, u'出血量（ml）')
			ws.write(0, 13, u'异体血（ml）')
			ws.write(0, 14, u'术中并发症')
			ws.write(0, 15, u'术中备注')
			ws.write(0, 16, u'术后并发症')
			ws.write(0, 17, u'动脉栓塞（方式')
			ws.write(0, 18, u'动脉栓塞（动脉名称）')
			ws.write(0, 19, u'经皮骨水泥加强（节段）')
			ws.write(0, 20, u'经皮骨水泥加强（部位）')
			ws.write(0, 21, u'支具支持治疗（支具类型）')
			ws.write(0, 22, u'支具支持治疗（开始年月）')
			ws.write(0, 23, u'放疗（总剂量 Gy）')
			ws.write(0, 24, u'放疗（疗程）')
			ws.write(0, 25, u'放疗（开始日期）')
			ws.write(0, 26, u'化疗（方案）')
			ws.write(0, 27, u'化疗（开始日期）')
			ws.write(0, 28, u'其他治疗（药物）')
			ws.write(0, 29, u'其他治疗（开始日期）')
			ws.write(0, 30, u'其他治疗（结束日期）')
			ws.write(0, 31, u'其他描述')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.surgery_date)
				ws.write(row_num, 3, obj.surgeon)
				ws.write(row_num, 4, (obj.get_approach_display() or ''))
				ws.write(row_num, 5, (obj.get_location_display() or ''))
				ws.write(row_num, 6, (obj.get_method_display() or ''))
				ws.write(row_num, 7, (obj.envelope_damage or ''))
				ws.write(row_num, 8, obj.sacrifice)
				ws.write(row_num, 9, obj.bone_cement)
				ws.write(row_num, 10, obj.radiofrequency)
				ws.write(row_num, 11, obj.total_time)
				ws.write(row_num, 12, obj.bleeding_vol)
				ws.write(row_num, 13, obj.allogeneic_blood)
				ws.write(row_num, 14, obj.surgery_complication)
				ws.write(row_num, 15, obj.surgery_comment)
				ws.write(row_num, 16, (obj.get_post_complication_display() or ''))
				ws.write(row_num, 17, obj.arterial_embolization_method)
				ws.write(row_num, 18, obj.arterial_embolization_name)
				ws.write(row_num, 19, obj.bone_cement_num)
				ws.write(row_num, 20, (obj.get_bone_cement_location_display() or ''))
				ws.write(row_num, 21, (obj.get_support_therapy_type_display() or ''))
				ws.write(row_num, 22, obj.support_therapy_start_date)
				ws.write(row_num, 23, obj.radiotherapy_dose)
				ws.write(row_num, 24, obj.radiotherapy_course)
				ws.write(row_num, 25, obj.radiotherapy_start_date)
				ws.write(row_num, 26, obj.chemotherapy_plan)
				ws.write(row_num, 27, obj.chemotherapy_start_date)
				ws.write(row_num, 28, (obj.get_other_treatment_drug_display() or ''))
				ws.write(row_num, 29, obj.other_treatment_start_date)
				ws.write(row_num, 30, obj.other_treatment_end_date)
				ws.write(row_num, 31, obj.comment)
				row_num += 1
		if db_name == 'test':
			all_objs =  Test.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'项目日期')
			ws.write(0, 3, u'项目名称')
			ws.write(0, 4, u'结果描述')
			ws.write(0, 5, u'诊断结论')
			ws.write(0, 6, u'是否术前检查')
			ws.write(0, 7, u'WBB分期(1-12)')
			ws.write(0, 8, u'WBB分期(A-F)')
			ws.write(0, 9, u'CT病变性质')
			ws.write(0, 10, u'X光顺列')
			ws.write(0, 11, u'塌陷')
			ws.write(0, 12, u'后外侧受累')
			ws.write(0, 13, u'椎动脉受累')
			ws.write(0, 14, u'Enneking分期')
			ws.write(0, 15, u'备注')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.project_date)
				ws.write(row_num, 3, obj.project_name)
				ws.write(row_num, 4, obj.result_discription)
				ws.write(row_num, 5, obj.diagosis)
				ws.write(row_num, 6, (obj.get_pre_test_display() or ''))
				ws.write(row_num, 7, obj.wbb_1_12)
				ws.write(row_num, 8, obj.wbb_A_F)
				ws.write(row_num, 9, (obj.get_CT_property_display() or ''))
				ws.write(row_num, 10, (obj.get_X_ray_display() or ''))
				ws.write(row_num, 11, (obj.get_collapse_display() or ''))
				ws.write(row_num, 12, (obj.get_lateral_involvement_display() or ''))
				ws.write(row_num, 13, obj.vertebral_artery_involvement)
				ws.write(row_num, 14, obj.enneking)
				ws.write(row_num, 15, obj.comment)
				row_num += 1
		if db_name == 'followup':
			all_objs =  FollowUp.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'主诉')
			ws.write(0, 3, u'复发')
			ws.write(0, 4, u'转移')
			ws.write(0, 5, u'内固定松动')
			ws.write(0, 6, u'内固定断裂')
			ws.write(0, 7, u'CT融合')
			ws.write(0, 8, u'随访方式')
			ws.write(0, 9, u'死亡日期')
			ws.write(0, 10, u'随访日期')
			ws.write(0, 11, u'备注')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.major_complain)
				ws.write(row_num, 3, (obj.get_recurrence_display() or ''))
				ws.write(row_num, 4, (obj.get_transfer_display() or ''))
				ws.write(row_num, 5, (obj.get_fixation_loose_display() or ''))
				ws.write(row_num, 6, (obj.get_fixation_break_display() or ''))
				ws.write(row_num, 7, (obj.get_CT_fusion_display() or ''))
				ws.write(row_num, 8, (obj.get_method_display() or ''))
				ws.write(row_num, 9, obj.DOD)
				ws.write(row_num, 10, obj.followup_date)
				ws.write(row_num, 11, obj.comment)
				row_num += 1
		if db_name == 'questionnaire':
			all_objs =  Questionnaire.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
			objs = [all_objs[int(idx)] for idx in indexes]
			ws.write(0, 0, u'姓名')
			ws.write(0, 1, u'病历号')
			ws.write(0, 2, u'EQ5D-1')
			ws.write(0, 3, u'EQ5D-2')
			ws.write(0, 4, u'EQ5D-3')
			ws.write(0, 5, u'EQ5D-4')
			ws.write(0, 6, u'EQ5D-5')
			ws.write(0, 7, u'问卷日期')

			row_num = 1

			for obj in objs:
				ws.write(row_num, 0, obj.name)
				ws.write(row_num, 1, obj.EMR_id)
				ws.write(row_num, 2, obj.EQ5D_1)
				ws.write(row_num, 3, obj.EQ5D_2)
				ws.write(row_num, 4, obj.EQ5D_3)
				ws.write(row_num, 5, obj.EQ5D_4)
				ws.write(row_num, 6, obj.EQ5D_5)
				ws.write(row_num, 7, obj.date)
				row_num += 1

		wb.close()
		output.seek(0)
		response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		response['Content-Disposition'] = 'attachment; filename=download.xlsx'
		return response
	else:
		response = HttpResponse("Not Found")
		response.status_code = 404
		return response


@login_required
def db_add_edit(request,DB_ID,mode,object_id=None,instance_id=None):
	db_name = DB_ID
	title=''
	opt = request.GET.get('opt', '')

	if object_id:
		curr_patient = get_object_or_404(Patient.objects.all(),DB_ID=object_id)

	if request.POST:
		if request.POST.get('cancel', None):
			#return HttpResponse('<script type="text/javascript">window.close();window.opener.location.reload(true);</script>')	
			return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.reload(true);}else{window.location.href="/dashboard/";window.opener.location.reload(true);}</script>' )

		if db_name == 'patient':
			if  mode == 'add':
				targetObj = Patient()
				targetForm = NewPatientForm(request.POST,instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = PatientForm(request.POST,instance=targetObj)
		elif db_name == 'cancer':
			if  mode == 'add':
				targetObj = Cancer()
				targetForm = CancerForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Cancer.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = CancerForm(request.POST,instance=targetObj)
		elif db_name == 'symptom':
			if  mode == 'add':
				targetObj = Symptom()
				targetForm = SymptomForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Symptom.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = SymptomForm(request.POST,instance=targetObj)
		elif db_name == 'treatment':
			if  mode == 'add':
				targetObj = Treatment()
				targetForm = TreatmentForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Treatment.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = TreatmentForm(request.POST,instance=targetObj)
		elif db_name == 'test':
			if  mode == 'add':
				targetObj = Test()
				targetForm = TestForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Test.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = TestForm(request.POST,instance=targetObj)
		elif db_name == 'followup':
			if  mode == 'add':
				targetObj = FollowUp()
				targetForm = FollowUpForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(FollowUp.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = FollowUpForm(request.POST,instance=targetObj)
		elif db_name == 'questionnaire':
			if  mode == 'add':
				targetObj = Questionnaire()
				targetForm = QuestionnaireForm(request.POST, instance=targetObj)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Questionnaire.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = QuestionnaireForm(request.POST,instance=targetObj)
		else:
			if request.user.is_authenticated:
				return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认数据库名称无误')
			else:
				return HttpResponseRedirect('/')
			#raise Exception('Unknow URL parameter')
		
		if targetForm.is_valid():
			new_instance = targetForm.save(commit=False)
			if object_id:
				new_instance.DB_ID = object_id
				new_instance.patient = curr_patient
			new_instance.save()
			targetForm.save_m2m()
			if object_id:
				return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))

	else:

		#get object instance

		#GET DBNAME	
		if db_name == 'patient':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name] 
				if object_id is None:
					targetForm = NewPatientForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {'name':targetObj.name,
								'EMR_id':targetObj.get_standard_EMR_id
								}
					targetForm = PatientForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id, pk=instance_id)
				title = '修改%s' % DB_NAME_DISPLAY[db_name]
				targetForm = PatientForm(instance=targetObj)
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/%s";window.opener.location.reload(true);}</script>' % (''.join(['?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join(['?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'cancer':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = CancerForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id

							}
					targetForm = CancerForm(initial=init_data)
			elif mode == 'edit' and object_id is not None  and instance_id is not None:
				title = '修改%s' % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(Cancer.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = CancerForm(instance=targetObj)

			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Cancer.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'symptom':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = SymptomForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id
							}
					targetForm = SymptomForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				title = '修改%s信息' % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(Symptom.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = SymptomForm(instance=targetObj)
			
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Symptom.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'treatment':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = TreatmentForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id
							}
					targetForm = TreatmentForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				title = '修改%s信息' % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(Treatment.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = TreatmentForm(instance=targetObj)
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Treatment.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'test':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = TestForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id
							}
					targetForm = TestForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				title = '修改%s信息' % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(Test.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = TestForm(instance=targetObj)
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Test.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'followup':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = FollowUpForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id
							}
					targetForm = FollowUpForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				title = '修改%s信息'  % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(FollowUp.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = FollowUpForm(instance=targetObj)
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(FollowUp.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')
		elif db_name == 'questionnaire':
			if mode == 'add':
				title = '新增%s条目' % DB_NAME_DISPLAY[db_name]
				if object_id is None:
					targetForm = QuestionnaireForm()
				else:
					targetObj = get_object_or_404(Patient.objects.all(),DB_ID=object_id)
			
					init_data = {
							'name':targetObj.name,
							'EMR_id':targetObj.get_standard_EMR_id
							}
					targetForm = QuestionnaireForm(initial=init_data)
			elif mode == 'edit' and object_id is not None and instance_id is not None:
				title = '修改%s信息' % DB_NAME_DISPLAY[db_name]
				targetObj = get_object_or_404(Questionnaire.objects.all(),DB_ID=object_id, pk=instance_id)
				targetForm = PatientForm(instance=targetObj)
			elif mode == 'delete' and object_id is not None  and instance_id is not None:
				targetObj = get_object_or_404(Questionnaire.objects.all(),DB_ID=object_id, pk=instance_id).delete()
				if object_id:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/get/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/get/%s";window.opener.location.reload(true);}</script>' % (''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([object_id,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
				else:
					return HttpResponse('<script type="text/javascript">if (window.opener){window.close();window.opener.location.href="/dashboard/db/%s";window.opener.location.reload(true);}else{window.location.href="/dashboard/db/%s";window.opener.location.reload(true);}</script>' % (''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]),''.join([db_name,'/',new_instance.DB_ID,'/?banner=success_',u'保存成功!'.encode('utf-8').decode('utf-8')]) ))
			else:
				if request.user.is_authenticated:
					return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认操作名称无误')
				else:
					return HttpResponseRedirect('/')
				#raise Exception('Unknow URL parameter')

		else:
			if request.user.is_authenticated:
				return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认数据库名称无误')
			else:
				return HttpResponseRedirect('/')
			#raise Exception('Unknow URL parameter')

		args = {}
		args.update(csrf(request))
		args['db_name']= db_name
		args['targetForm'] = targetForm
		args['user'] = request.user
		args['title'] = title
		args['object_id'] = object_id
		if object_id:
			args['curr_patient'] =curr_patient
		args['banner'] = request.GET.get('banner', '').split('_')

		return render_to_response('DBView/db_add_edit.html',args)



@login_required
def general_search(request):
	#get patient list, privacy should be considered
	if is_guest(request.user):
		patients =  Patient.objects.all().filter(visible_to=1).order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')
	else:
		patients =  Patient.objects.all().order_by('DB_ID')#Patient.objects.filter(created_by__NTID__iexact=request.user.username).order_by('-created_date')

	#other related table fields
	fields = list()
	#for patient in patients:
		#cancer_cell = []
		#cancers = Cancer.objects.filter(DB_ID__iexact=patient.DB_ID).order_by('DB_ID')
		#for field in cancer._meta.get_all_field_names():
		#	if getattr(cancer,field.name)):
				#try:
					#str_value = str(getattr(cancer,field.name))
					#cancer_cell.append(str_value)
		#		pass
		#symptom = Symptom.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#treatement = Treatment.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#test = Test.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#followup = FollowUp.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')
		#questionnaire = Questionnaire.objects.filter(DB_ID__iexact=objs.DB_ID).order_by('DB_ID')

	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	args['patients'] = patients
	#args['cancers'] = cancers
	#args['symptom'] = symptom
	#args['test'] = test
	#args['followup'] = followup
	#args['questionnaire'] = questionnaire
	args['banner'] = request.GET.get('banner', '').split('_')

	return render_to_response('consoleView/general_search.html',args)

def detail(request, DB_ID):

	if DB_ID:

		if is_guest(request.user):
			curr_patient = get_object_or_404(Patient.objects.all(),DB_ID=DB_ID,visible_to=1)
		else:
			curr_patient = get_object_or_404(Patient.objects.all(),DB_ID=DB_ID)

		if request.POST:
			if 'sendEmail' in request.POST:
				if request.user.email:
					fromemail = request.user.email
				else:
					fromemail = request.user.username
				header = request.POST['subject']
				to = request.POST['emailto'].split(',')
				content = request.POST['content']
				msg = EmailMultiAlternatives(header, content, fromemail, to)
				msg.content_subtype = "html"
				msg.send()

				return HttpResponseRedirect('/dashboard/get/%s/?banner=success_邮件发送成功!' % DB_ID)#('/dashboard/confirm/?h=success&t=Email Sent! &b1=back&b2=dashboard')

			if 'delete_instance' in request.POST:
				if request.user.is_authenticated():
					get_object_or_404(Experiment, experiment_id=experiment.experiment_id).delete()
		else:
			patient = get_object_or_404(Patient, DB_ID=DB_ID)

			#other related table fields
			cancers = Cancer.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
			symptoms = Symptom.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
			treatments = Treatment.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
			tests = Test.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
			followups = FollowUp.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')
			questionnaires = Questionnaire.objects.filter(DB_ID__iexact=DB_ID).order_by('DB_ID')

			#get diagnosis for this patient
			similar_patients = []
			if cancers:
				patient_diagnosis = [cancer.diagnosis for cancer in cancers]

				if patient_diagnosis[0]:
					similar_entries = Cancer.objects.filter(diagnosis__in=patient_diagnosis).exclude(DB_ID=DB_ID).order_by('DB_ID')
					patient_seen = []
					for i in similar_entries:
						if i.DB_ID not in patient_seen:
							similar_patients.append(i)
						patient_seen.append(i.DB_ID)

			args = {}
			args.update(csrf(request))
			args['user'] = request.user
			args['patient'] = patient
			args['cancers'] = cancers
			args['symptoms'] = symptoms
			args['treatments'] = treatments
			args['tests'] = tests
			args['followups'] = followups
			args['questionnaires'] = questionnaires

			args['similar_patients'] = similar_patients
			args['banner'] = request.GET.get('banner', '').split('_')

			return render(request, 'detailView/detail.html', args)
	else:
		HttpResponseRedirect('/dashboard/')


@login_required
def mark(request,DB_ID):
	if DB_ID:

		curr_patient = get_object_or_404(Patient.objects.all(),DB_ID=DB_ID)

    	if request.method == 'POST':
			if not curr_patient.tagged:
				curr_patient.tagged = True
				curr_patient.save()
				return HttpResponseRedirect('/dashboard/get/%s/?banner=success_%s!' % (DB_ID,u"成功标记该病人".encode('utf-8').decode('utf-8')))#('/dashboard/confirm/?h=success&t=Email Sent! &b1=back&b2=dashboard')
			else:
				curr_patient.tagged = False
				curr_patient.save()
				return HttpResponseRedirect('/dashboard/get/%s/?banner=success_%s!' % (DB_ID,u"成功取消标记".encode('utf-8').decode('utf-8')))#('/dashboard/confirm/?h=success&t=Email Sent! &b1=back&b2=dashboard')

	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect('/dashboard/?banner=warning_URL地址不存在！_请确认病人ID无误')
		else:
			return HttpResponseRedirect('/')

#?h=success&t=test-title&c=test-content&b1=back&b2=console
def confirm(request):

	candidate_buttons = {
	'back': "<a class=\"btn btn-primary btn-lg\" style=\"margin-right: 20px;\" onclick=\"goBack()\">Go Back</a>",
	'main':"<a href=\"/\" class=\"btn btn-primary btn-lg\" style=\"margin-right: 20px;\">Main Page</a>",
	'close':"<a class=\"btn btn-primary btn-lg\" style=\"margin-right: 20px;\" onclick=\"window.close();\">Close</a>",
	'dashboard':"<a href=\"/dashboard/\" class=\"btn btn-primary btn-lg\" style=\"margin-right: 20px;\">My Dashboard</a>",
	'contact':"<a href=\"/contact/\" class=\"btn btn-primary btn-lg\" style=\"margin-right: 20px;\">Contact</a>"
	}

	#button section
	button_section = ''
	for i in range(1,4):
		incoming_p = 'b'+str(i)
		if request.GET.get(incoming_p, '') in candidate_buttons:
			button_section += candidate_buttons[request.GET.get(incoming_p, '')]

	args = {}
	args.update(csrf(request))
	args['head'] = request.GET.get('h', '')
	args['title'] = request.GET.get('t', '')
	args['content'] = request.GET.get('c', '')
	args['buttons'] = button_section #b1,b2

	args['user'] = request.user
	return render_to_response('infoView/confirm.html',args)
		

######################registered template filters##########################
@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def key(d, key_name):
	try:
		value = d[key_name]
	except:
		from django.conf import settings

		value = settings.TEMPLATE_STRING_IF_INVALID

	return value


