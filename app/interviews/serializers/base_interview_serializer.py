from . import serializers, InterviewEmployeeSerializer, Interview

class BaseInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = [
            'id',
            'candidate',
            'passed',
            'assigned_at',
            'created_at'
        ]

    def get_candidate(self, interview):
        """ Receive candidate information """

        serializer = InterviewEmployeeSerializer(
            interview.candidate, read_only=True,
            context={'company_id': interview.vacancy.company.id }
        )
        return serializer.data
