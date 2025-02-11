def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    x_real_ip = request.META.get("HTTP_X_REAL_IP")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    elif x_real_ip:
        ip = x_real_ip.strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
