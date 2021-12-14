from django.db import models

from apps.core.models import TimeStamped


class TaskDesignation(TimeStamped):
    date = models.DateField()
    staff = models.ForeignKey(
        "authentication.Staff", on_delete=models.SET_NULL, blank=True, null=True
    )
    client = models.ForeignKey(
        "authentication.Client", on_delete=models.SET_NULL, blank=True, null=True
    )
    managers_note = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Task designation for {self.staff} - client({self.client})"


class AssignmentNote(TimeStamped):
    """
    Assignment Note model
    """

    task_designation = models.ForeignKey(
        TaskDesignation,
        related_name="task_designation_assignments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    note = models.TextField()

    def __str__(self):
        return self.note
