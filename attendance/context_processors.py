def active_school_context(request):
    return {
        "active_school": None,
        "platform_name": "Mwandet Digital",
        "platform_short_name": "M.D",
        "school_display_name": "Mwandet Secondary",
        "platform_brand_name": "Mwandet Digital",
        "platform_brand_short_name": "M.D",
        "platform_brand_logo": "assets/img/mwandeticon.jpg",
        "platform_brand_logo_no_bg": "assets/img/mwandeticon-no-bg.png",
        "platform_brand_banner": "assets/img/mwandet-banner.jpeg",
    }


def portal_roles(request):
    user = request.user
    if not user.is_authenticated:
        return {
            "can_access_teacher_hub": False,
            "can_access_academic_office": False,
            "can_access_management": False,
            "can_access_platform_admin": False,
        }

    group_names = set(user.groups.values_list("name", flat=True))
    is_superuser = user.is_superuser

    return {
        "can_access_teacher_hub": is_superuser or bool(group_names.intersection({"Teachers", "Management", "Academic Office"})),
        "can_access_academic_office": is_superuser or bool(group_names.intersection({"Management", "Academic Office"})),
        "can_access_management": is_superuser or "Management" in group_names,
        "can_access_platform_admin": is_superuser,
    }
