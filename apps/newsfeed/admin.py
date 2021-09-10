from django.contrib import admin


from apps.newsfeed.models import NewsFeed, NewsFeedComment


class NewsFeedAdmin(admin.ModelAdmin):
    model = NewsFeed
    list_display = ("title", "body", "publish_to")

    class Media:
        js = (
            "grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
            "grappelli/tinymce_setup/tinymce_setup.js",
        )


admin.site.register(NewsFeed, NewsFeedAdmin)
