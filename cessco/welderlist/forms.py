from django import forms

from .models import Welder
from .models import PerformanceQualification
# core.models import fNumberLov

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class WelderCreateForm(forms.ModelForm):
	class Meta:
		model = Welder
		Welder.first_name = forms.CharField(max_length=128)
		Welder.last_name = forms.CharField(max_length=128)
		Welder.absa_number = forms.CharField(max_length=16)

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('submit', 'Save Welder'))


class PerformanceQualificationCreateForm(forms.ModelForm):
	class Meta:
		model = PerformanceQualification
		# PerformanceQualification.f_number = forms.ModelChoiceField(queryset=core.fNumberLov.objects.all())


	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('submit', 'Save PerformanceQualification'))

