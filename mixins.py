from django.http import JsonResponse
from django.contrib import messages

class AjaxableFormMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super(AjaxableFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': 'Submit success',
            }
            return JsonResponse(data)
        else:
            return response


class DeleteAjaxMixin(object):
    """
    Mixin which deletes object if request is not ajax request.
    """

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            messages.success(request, self.success_message)
        return super(DeleteAjaxMixin, self).delete(request, *args, **kwargs)
