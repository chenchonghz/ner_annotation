from django.utils.html import escape
from django.db.models import Q
from models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire  # STC

from selectable.base import ModelLookup
from selectable.registry import registry

'''
class ExperimentTitleLookup(ModelLookup):
    model = Experiment
    search_fields = ('title__icontains', )
    def get_item_label(self, item):
	if item.created_by:
                return "%s (%s)" % (item.title,item.created_by)
        else:
                return "%s (%s)" % (item.title,'-')

    def get_item_value(self, item):
        # Display for currently selected item
        return item.title
registry.register(ExperimentTitleLookup)



class ProjectLookup(ModelLookup):
    model = Experiment
    search_fields = ('project_name__icontains', )

    def get_query(self, request, term):
        qs = Experiment.objects.all()#super(ProjectLookup, self).get_query(request, term)
        fs = []
	met = []
	for i in qs:
		name = i.project_name
		people = i.created_by
		check = str(name)+"-"+str(people)
		if check not in met:
			met.append(check)
			fs.append(i)
	return fs#disp.distinct()

    def get_item_value(self, item):
        # Display for currently selected item
        return item.project_name


#    def get_query(self, request, term):
#    	qs = super(ProjectLookup, self).get_query(request, term)
#	disp = qs.values_list( "project_name",'created_by')#qs.values_list( "project_name", flat=True)
#    	return disp.distinct()

#    def get_item_id(self, item):
#    	return item

    def get_item_label(self, item):
        if item.created_by:
                return u"%s - %s" % (item.project_name,item.created_by)
        else:
                return u"%s - %s" % (item.project_name,'-')


registry.register(ProjectLookup)


class InvestigatorLookup(ModelLookup):
    model = IDMSUser
    search_fields = ('FirstName__icontains', 'NTID__icontains', 'LastName__icontains')
    filters = {'approvalStatus': True, }
    def get_item_label(self, item):
    	return "%s %s (%s)" %(item.FirstName, item.LastName, item.EmailAddress)
registry.register(InvestigatorLookup)


class CellmodelLookup(ModelLookup):
    model = CcleLibrary
    search_fields = ('CCLE_name__icontains', )
    filters = {'approvalStatus': True, }

registry.register(CellmodelLookup)

class ShrnaLookup(ModelLookup):
    model = ShrnaLibrary
    search_fields = ('LibName_Full__icontains', )
    filters = {'approvalStatus': True, }
    
 #   def get_query(self, request, term):
#	results = super(ShrnaLookup, self).get_query(request, term)
  #      state = request.GET.get('shrna', '')
  #      if state:
 #           results = results.filter(state=state)
#        return results

    def get_item_label(self, item):
        return "%s (%s)" %(item.LibName, item.LibName_Full)
registry.register(ShrnaLookup)

'''
