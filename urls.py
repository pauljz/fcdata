import config
import enums

def generator():
    rankingurl = "http://api.foundationcenter.org/research-dev/v1.0/foundations/top50/rankings.json"
    vals = 5 * [None]

    vals[0] = "key=%s" % config.apikey

    for year in enums.year:
        vals[1] = "year=%s" % year

        for rank_by in enums.rank_by:
            vals[2] = "rank_by=%s" % rank_by

            for organization_type in enums.organization_type:
                vals[3] = "organization_type=%s" % organization_type

                for funder_location in enums.funder_location:
                    vals[4] = "funder_location=%s" % funder_location
                    url = rankingurl + "?" + "&".join(vals)
                    yield url