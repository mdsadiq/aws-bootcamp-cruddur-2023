from datetime import datetime, timedelta, timezone
from opentelemetry import trace
# from aws_xray_sdk.core import xray_recorder

tracer = trace.get_tracer("user.activities")
class UserActivities:
  def __init__(self, request):
      #self.xray_recorder = xray_recorder
      self.request = request

  def run(self, user_handle):
    # try:
      # xray ---
      # parent_subsegment = xray_recorder.begin_subsegment('user_activities_sub')
      # parent_subsegment.put_annotation('url', self.request.url)

      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      # xray_dict = { 'now': now }
      # parent_subsegment.put_metadata('now', xray_dict, 'user_activities')
      # parent_subsegment.put_metadata('method', self.request.method, 'http')
      # parent_subsegment.put_metadata('url', self.request.url, 'http')
      # with tracer.start_as_current_span("home-activities.mock-data"):
      #   span = trace.get_current_span()
      #   span.set_attribute("userId", user_handle)
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        # subsegment = xray_recorder.begin_subsegment('user_activities_nested_subsegment')
        now = datetime.now()
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results
        return model