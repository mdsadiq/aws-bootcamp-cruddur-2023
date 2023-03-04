from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class UserActivities:
  def __init__(self, request):
      #self.xray_recorder = xray_recorder
      self.request = request

  def run(self, user_handle):
    try:
      # xray ---
      parent_subsegment = xray_recorder.begin_subsegment('user_activities_sub')
      parent_subsegment.put_annotation('url', self.request.url)

      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      xray_dict = { 'now': now }
      parent_subsegment.put_metadata('now', xray_dict, 'user_activities')
      parent_subsegment.put_metadata('method', self.request.method, 'http')
      parent_subsegment.put_metadata('url', self.request.url, 'http')
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        try:
          subsegment = xray_recorder.begin_subsegment('user_activities_nested_subsegment')
          now = datetime.now()
          results = [{
            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
            'handle':  'Andrew Brown',
            'message': 'Cloud is fun!',
            'created_at': (now - timedelta(days=1)).isoformat(),
            'expires_at': (now + timedelta(days=31)).isoformat()
          }]
          model['data'] = results
          xray_dict['results'] = len(model['data'])
          subsegment.put_metadata('results', xray_dict, 'user_activities')
        except Exception as e:
          # Raise the error in the segment
          raise e
        finally:  
          xray_recorder.end_subsegment()
      subsegment = xray_recorder.begin_subsegment('mock-data')
      # xray ---
      dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
      }
      subsegment.put_metadata('key', dict, 'namespace')
      xray_recorder.end_subsegment()
    finally:
    #   # Close the segment
      xray_recorder.end_subsegment()
    return model