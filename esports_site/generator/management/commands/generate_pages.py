import requests
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.conf import settings
from pathlib import Path


class Command(BaseCommand):
    help = "Generate static HTML pages for esports matches"

    def handle(self, *args, **kwargs):
        base_url = "https://api.pandascore.co/matches"
        headers = {
            "Authorization": f"Bearer {settings.PANDASCORE_API_KEY}"
        }

        dates = {
            "yesterday": datetime.utcnow() - timedelta(days=1),
            "today": datetime.utcnow(),
            "tomorrow": datetime.utcnow() + timedelta(days=1),
        }

        output_dir = Path(settings.BASE_DIR) / "site"
        output_dir.mkdir(exist_ok=True)

        for name, date in dates.items():
            date_str = date.strftime("%Y-%m-%d")

            params = {
                "range[begin_at]": f"{date_str}T00:00:00Z,{date_str}T23:59:59Z",
                "sort": "begin_at",
                "page[size]": 10
            }

            response = requests.get(base_url, headers=headers, params=params)
            data = response.json()



            matches = []
            for match in data:
                if not isinstance(match, dict):
                    continue

                matches.append({
                    "name": match.get("name"),
                    "league": (match.get("league") or {}).get("name"),
                    "begin_at": match.get("begin_at"),
                })

            html = render_to_string("matches.html", {
                "matches": matches,
                "page_name": name.capitalize(),
                "seo_title": f"{name.capitalize()} Esports Matches",
                "seo_description": f"All esports matches for {name}"
            })

            file_path = output_dir / f"{name}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)

            self.stdout.write(self.style.SUCCESS(f"Generated {file_path}"))
