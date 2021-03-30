from typing import List, Optional
from django.utils.decorators import method_decorator

from herald import registry
from herald.base import EmailNotification

from apps.gpg.models import PropertyDetail


class ContextMixin:
    def get_context_data(self):
        context = super().get_context_data()
        context["domain"] = Site.objects.get_current()
        context["protocol"] = settings.HTTP_PROTOCOL
        return context


class ModelMixin:
    model = None
    pk_kwargs = "pk"

    def __init__(self, *args, **kwargs):
        self.kwargs_pk = kwargs.pop(self.pk_kwargs, None)
        if not self.kwargs_pk:
            if args:
                self.kwargs_pk = args[0].pk
        if not self.model:
            raise NotImplementedError("Must set `model`")

        self.obj = self.get_object()

    def get_object(self):
        print(self.kwargs_pk)
        return self.model.objects.get(**{self.pk_kwargs: self.kwargs_pk})


class BaseEmailNotification(ContextMixin, EmailNotification):
    def __init__(
        self,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        to_emails: Optional[List[str]] = None,
        content: Optional[str] = None,
        context: Optional[dict] = None,
        *args,
        **kwargs,
    ):
        if to_emails:
            self.to_emails = to_emails
        if cc:
            self.cc = cc
        if bcc:
            self.bcc = bcc
        if context:
            self.context = context


class BaseModelEmailNotification(ModelMixin, BaseEmailNotification):
    pass
