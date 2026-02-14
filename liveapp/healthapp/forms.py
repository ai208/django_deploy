from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['condition','mental_status','weight','wakeup_time','bed_time','sleep_duration','memo']
        labels ={
            'condition':'体調',
            'mental_status':'精神状態',
            'weight':'体重(kg)',
            'wakeup_time':'起床時間',
            'bed_time':'就寝時間(編集可能)',
            'sleep_duration':'睡眠時間(h)',
            'memo':'メモ',
            }
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)