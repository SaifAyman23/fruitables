def userEmail(request):
    if request.user.is_authenticated:
        return {'email':request.user.email}
    return {'email':None}    