class IpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)       
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if (view_func.__name__=="click" or view_func.__name__=="index"):
            view_kwargs['ip'] = self.get_client_ip(request)

    def get_client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip