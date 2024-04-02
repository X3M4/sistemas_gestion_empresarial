# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports associations members, teams and events",
    "version": "17.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "category": "Sports",
    "author": "<Chema Fernández>, Domatix",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["your-github-login"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    
    "data": [
            "data/sport_issue_tag_data.xml",
            "data/ir_cron.xml",
            "security/groups.xml",
            "security/ir.model.access.csv",
             "views/sport_issue_views.xml",
             "views/sport_clinic_views.xml",
             "views/sport_issue_tag_views.xml",
             "views/sport_team_views.xml",
             "views/sport_sport_views.xml",
             "views/sport_player_views.xml",
             "views/sport_league_views.xml",
             "views/sport_match_view.xml",
             "views/sport_issue_menu.xml",
             "wizards/sport_create_issue.xml",
             ],
}