# test_video.py created by sylvi at 2021/4/23 9:37 AM
from django.test import TestCase, Client
from django.urls import reverse
from django.utils.dateparse import parse_duration, parse_datetime
from rest_framework import status

from .models import Video
from .serializers import VideoSerializer


# initialize the APIClient app
client = Client()

dict_vids = {
    "kind": "youtube#videoListResponse",
    "etag": "b1ursoj_XSUrcGA9n0f3KvHL78I",
    "items": [
        {
            "kind": "youtube#video",
            "etag": "Vn5SyRG_GC7eaQhNQw_1Rxj6ScM",
            "id": "fwQci1cRiFU",
            "snippet": {
                "publishedAt": "2018-05-06T08:19:13Z",
                "channelId": "UC8R8FRt1KcPiR-rtAflXmeg",
                "title": "Effective Ways to Practice Arpeggios",
                "description": "➡ Thank you for supporting me on Patreon!\nhttps://www.patreon.com/nahresol\n\nNew Warm-Ups in ii-V-I: https://youtu.be/jKMNIB9sk18\n\nIn today's Practice Notes 59, I share ways to practice arpeggios that I believe are effective and efficient.  Although this video is very piano specific, there are some concepts that can translate over to other instruments as well.  These points of conscious practicing really helped me improve my piano technique over the years.\n\nThe two pieces of music I use to demonstrate these practice methods is Chopin's Etude Op. 10 No. 1 and Exercise 8A from my Modified Chopin Exercises book.\n\n➡ Get the Modified Chopin Exercises Book:  https://bit.ly/2HBpOk1\n\nHere are the time stamps for the video to help you navigate and reference the different sections:\n00:45 -- Rhythms and Accenting\n02:50 -- Why Rhythms and Accenting are Effective\n03:44 -- Organizing Hand Positions\n04:15 -- Blocking\n05:43 -- Micro-Adjustments and Relaxation\n06:29 -- Elbow Movement\n08:34 -- Kill Two Birds w/ One Stone\n09:00 -- Teeter-Totter\n10:09 -- Looping\n10:45 -- Repeating Notes\n\nRhythm drills for practice: https://www.youtube.com/watch?v=sTq92MkSWQ4\n\nInstagram @nahresol\nTwitter @nahresol\nFacebook @practicenotes\n\nKeyboard: https://amzn.to/2NbPjYA\nCamera: https://amzn.to/2BE54X3\nLens: https://amzn.to/2NaQiby\n\nSubscribe to the channel to follow my uploads:\nPRACTICE NOTES: https://www.youtube.com/playlist?list=PL0UfT1ar7nMclK9fh4hVcbwB-GJcUVzvY\nSOUND BANK: https://www.youtube.com/playlist?list=PL0UfT1ar7nMc-RQEUNIo0kRIBohUizwFn\nORIGINALS: https://www.youtube.com/playlist?list=PL0UfT1ar7nMdpYHYL2dw07s_W4xCMobpV\n\nAs always, thank you so much for watching, and thank you to all of you that leave comments.\n\nThis video is not sponsored and features no sponsored products but some links above are affiliate links (you don't pay more, but I earn a small commission for my recommendation).",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/fwQci1cRiFU/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/fwQci1cRiFU/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/fwQci1cRiFU/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/fwQci1cRiFU/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "https://i.ytimg.com/vi/fwQci1cRiFU/maxresdefault.jpg",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "Nahre Sol",
                "tags": [
                    "how to practice arpeggios",
                    "how to improve piano",
                    "how to improve piano technique",
                    "how to practice piano",
                    "nahre sol",
                    "conscious practicing",
                    "how to compose",
                    "modern piano",
                    "how to write music",
                    "advanced music theory",
                    "advanced piano",
                    "advanced piano lesson",
                    "intermediate piano lesson",
                    "piano teacher",
                    "how to play piano",
                    "professional piano",
                    "pianist composer",
                    "modern harmony",
                    "contemporary harmony",
                    "modified chopin",
                    "chopin etude",
                    "how to practice chopin etude op 10 no 1",
                    "piano arpeggios"
                ],
                "categoryId": "10",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "Effective Ways to Practice Arpeggios",
                    "description": "➡ Thank you for supporting me on Patreon!\nhttps://www.patreon.com/nahresol\n\nNew Warm-Ups in ii-V-I: https://youtu.be/jKMNIB9sk18\n\nIn today's Practice Notes 59, I share ways to practice arpeggios that I believe are effective and efficient.  Although this video is very piano specific, there are some concepts that can translate over to other instruments as well.  These points of conscious practicing really helped me improve my piano technique over the years.\n\nThe two pieces of music I use to demonstrate these practice methods is Chopin's Etude Op. 10 No. 1 and Exercise 8A from my Modified Chopin Exercises book.\n\n➡ Get the Modified Chopin Exercises Book:  https://bit.ly/2HBpOk1\n\nHere are the time stamps for the video to help you navigate and reference the different sections:\n00:45 -- Rhythms and Accenting\n02:50 -- Why Rhythms and Accenting are Effective\n03:44 -- Organizing Hand Positions\n04:15 -- Blocking\n05:43 -- Micro-Adjustments and Relaxation\n06:29 -- Elbow Movement\n08:34 -- Kill Two Birds w/ One Stone\n09:00 -- Teeter-Totter\n10:09 -- Looping\n10:45 -- Repeating Notes\n\nRhythm drills for practice: https://www.youtube.com/watch?v=sTq92MkSWQ4\n\nInstagram @nahresol\nTwitter @nahresol\nFacebook @practicenotes\n\nKeyboard: https://amzn.to/2NbPjYA\nCamera: https://amzn.to/2BE54X3\nLens: https://amzn.to/2NaQiby\n\nSubscribe to the channel to follow my uploads:\nPRACTICE NOTES: https://www.youtube.com/playlist?list=PL0UfT1ar7nMclK9fh4hVcbwB-GJcUVzvY\nSOUND BANK: https://www.youtube.com/playlist?list=PL0UfT1ar7nMc-RQEUNIo0kRIBohUizwFn\nORIGINALS: https://www.youtube.com/playlist?list=PL0UfT1ar7nMdpYHYL2dw07s_W4xCMobpV\n\nAs always, thank you so much for watching, and thank you to all of you that leave comments.\n\nThis video is not sponsored and features no sponsored products but some links above are affiliate links (you don't pay more, but I earn a small commission for my recommendation)."
                }
            },
            "contentDetails": {
                "duration": "PT11M30S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "False",
                "licensedContent": True,
                "contentRating": {},
                "projection": "rectangular"
            },
            "topicDetails": {
                "topicCategories": [
                    "https://en.wikipedia.org/wiki/Classical_music",
                    "https://en.wikipedia.org/wiki/Music"
                ]
            }
        },
        {
            "kind": "youtube#video",
            "etag": "4yz5P-4r262E6n1GK6HWZIwmxWE",
            "id": "LZie2QC5Jbc",
            "snippet": {
                "publishedAt": "2016-03-28T12:57:11Z",
                "channelId": "UCJ0yBou72Lz9fqeMXh9mkog",
                "title": "Quantum Operators",
                "description": "Quantum Operators for measurements of Energy, Position, and Momentum in Quantum Physics.  My Patreon page is at https://www.patreon.com/EugeneK",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/LZie2QC5Jbc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/LZie2QC5Jbc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/LZie2QC5Jbc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/LZie2QC5Jbc/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "https://i.ytimg.com/vi/LZie2QC5Jbc/maxresdefault.jpg",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "Physics Videos by Eugene Khutoryansky",
                "tags": [
                    "Quantum Operators",
                    "Quantum physics",
                    "Quantum Mechanics"
                ],
                "categoryId": "28",
                "liveBroadcastContent": "none",
                "defaultLanguage": "en",
                "localized": {
                    "title": "Quantum Operators",
                    "description": "Quantum Operators for measurements of Energy, Position, and Momentum in Quantum Physics.  My Patreon page is at https://www.patreon.com/EugeneK"
                },
                "defaultAudioLanguage": "en"
            },
            "contentDetails": {
                "duration": "PT21M46S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "True",
                "licensedContent": True,
                "contentRating": {},
                "projection": "rectangular"
            },
            "topicDetails": {
                "topicCategories": [
                    "https://en.wikipedia.org/wiki/Knowledge"
                ]
            }
        },
        {
            "kind": "youtube#video",
            "etag": "ueral0hyKkcZkaxkV5qcBmmyWGE",
            "id": "WJownYnZ1ZQ",
            "snippet": {
                "publishedAt": "2020-01-15T19:00:05Z",
                "channelId": "UCisoaS5VIOtmZL74_jPWCmQ",
                "title": "Maker: The Art of Terry Borman",
                "description": "A film that explores the life and work of world renowned luthier Terry Borman.  https://www.bormanviolins.com\n\n\nMusic in this video\nSong: The Tale of Tsar Saltan, Op. 57: Flight of the Bumble Bee\nArtist:  Scottish National Orchestra\nAlbum:  Russian Masterpieces\nLicensed to YouTube by:  NaxosofAmerica (on behalf of Chandos); UMPI, UMPG Publishing, BMG Rights Management, Warner Chappell, and 6 Music Rights Societies",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/WJownYnZ1ZQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/WJownYnZ1ZQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/WJownYnZ1ZQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/WJownYnZ1ZQ/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "https://i.ytimg.com/vi/WJownYnZ1ZQ/maxresdefault.jpg",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "BormanViolins",
                "tags": [
                    "violin making",
                    "luthier",
                    "terry borman"
                ],
                "categoryId": "10",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "Maker: The Art of Terry Borman",
                    "description": "A film that explores the life and work of world renowned luthier Terry Borman.  https://www.bormanviolins.com\n\n\nMusic in this video\nSong: The Tale of Tsar Saltan, Op. 57: Flight of the Bumble Bee\nArtist:  Scottish National Orchestra\nAlbum:  Russian Masterpieces\nLicensed to YouTube by:  NaxosofAmerica (on behalf of Chandos); UMPI, UMPG Publishing, BMG Rights Management, Warner Chappell, and 6 Music Rights Societies"
                },
                "defaultAudioLanguage": "en-US"
            },
            "contentDetails": {
                "duration": "PT25M7S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "False",
                "licensedContent": False,
                "contentRating": {},
                "projection": "rectangular"
            },
            "topicDetails": {
                "topicCategories": [
                    "https://en.wikipedia.org/wiki/Classical_music"
                ]
            }
        },
        {
            "kind": "youtube#video",
            "etag": "5WnLo3oIQ96xhJ5BC6FW6zFupew",
            "id": "l5XJdHfPc5o",
            "snippet": {
                "publishedAt": "2021-02-02T15:31:35Z",
                "channelId": "UCiawGYzxoZSPDLReSFETqeQ",
                "title": "Bach's C major prelude, deconstructed",
                "description": "Bach's prelude in C major from book one of 'The Well-Tempered Clavier' is one of the most recognisable pieces of piano music ever written. In this essay, I deconstruct the history, rhythm and harmony to try and work out why it has captivated musicians and listeners for centuries.\n\n▶ Support my channel: https://www.patreon.com/listeningin\n▶ Subscribe: https://bit.ly/2PlVaMS\n____________________\n▶ Website: http://www.barnabymartin.com\n▶ Twitter: https://twitter.com/BarnabyMartin\n\nFURTHER READING/RESEARCH\nKlavierbüchlein für Wilhelm Friedemann Bach: http://tinyurl.com/154z8h8a\nBach's Well-Tempered Clavier: The 48 Preludes and Fugues: https://www.amazon.co.uk/Bachs-Well-Tempered-Clavier-Preludes-Fugues/dp/0300178956/ref=sr_1_1?dchild=1&keywords=bach%27s+well-tempered+clavier+ledbetter&qid=1612254538&sr=8-1\n\nFURTHER WATCHING\nThat famous cello prelude, deconstructed [Vox]: https://www.youtube.com/watch?v=UIge2mYdTtM&t=526s\nAndrás Schiff on the recording of Bach's „The Well-Tempered Clavier\": https://www.youtube.com/watch?v=TdzLWKuo0YA",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/l5XJdHfPc5o/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/l5XJdHfPc5o/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/l5XJdHfPc5o/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/l5XJdHfPc5o/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "https://i.ytimg.com/vi/l5XJdHfPc5o/maxresdefault.jpg",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "Listening In",
                "tags": [
                    "Bach's C major prelude deconstructed",
                    "bach c major prelude",
                    "bach prelude",
                    "bach prelude analysis",
                    "bach c major",
                    "bach piano",
                    "J S Bach",
                    "bach piano analysis",
                    "prelude in c major",
                    "prelude in c major deconstructed",
                    "that famous cello prelude deconstructed",
                    "that famouse cello prelude",
                    "bach well tempered clavier",
                    "bach well tempered clavier prelude 1",
                    "bach prelude in c major",
                    "bach prelude in c major harpsichord",
                    "andras schiff"
                ],
                "categoryId": "10",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "Bach's C major prelude, deconstructed",
                    "description": "Bach's prelude in C major from book one of 'The Well-Tempered Clavier' is one of the most recognisable pieces of piano music ever written. In this essay, I deconstruct the history, rhythm and harmony to try and work out why it has captivated musicians and listeners for centuries.\n\n▶ Support my channel: https://www.patreon.com/listeningin\n▶ Subscribe: https://bit.ly/2PlVaMS\n____________________\n▶ Website: http://www.barnabymartin.com\n▶ Twitter: https://twitter.com/BarnabyMartin\n\nFURTHER READING/RESEARCH\nKlavierbüchlein für Wilhelm Friedemann Bach: http://tinyurl.com/154z8h8a\nBach's Well-Tempered Clavier: The 48 Preludes and Fugues: https://www.amazon.co.uk/Bachs-Well-Tempered-Clavier-Preludes-Fugues/dp/0300178956/ref=sr_1_1?dchild=1&keywords=bach%27s+well-tempered+clavier+ledbetter&qid=1612254538&sr=8-1\n\nFURTHER WATCHING\nThat famous cello prelude, deconstructed [Vox]: https://www.youtube.com/watch?v=UIge2mYdTtM&t=526s\nAndrás Schiff on the recording of Bach's „The Well-Tempered Clavier\": https://www.youtube.com/watch?v=TdzLWKuo0YA"
                },
                "defaultAudioLanguage": "en-GB"
            },
            "contentDetails": {
                "duration": "PT9M47S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "False",
                "licensedContent": True,
                "contentRating": {},
                "projection": "rectangular"
            },
            "topicDetails": {
                "topicCategories": [
                    "https://en.wikipedia.org/wiki/Classical_music"
                ]
            }
        },
        {
            "kind": "youtube#video",
            "etag": "JuJnZt-BgdUxv2Mz2yMJVu_ZCCk",
            "id": "DivuT0HpazQ",
            "snippet": {
                "publishedAt": "2019-10-29T20:50:52Z",
                "channelId": "UCXFXosD6iYS2hhlT2lmQpJQ",
                "title": "Dr Quantum   Double Slit Experiment   YouTube 1",
                "description": "",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/DivuT0HpazQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/DivuT0HpazQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/DivuT0HpazQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/DivuT0HpazQ/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    }
                },
                "channelTitle": "Vadim Chernov",
                "categoryId": "22",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "Dr Quantum   Double Slit Experiment   YouTube 1",
                    "description": ""
                }
            },
            "contentDetails": {
                "duration": "PT5M42S",
                "dimension": "2d",
                "definition": "sd",
                "caption": "False",
                "licensedContent": False,
                "contentRating": {},
                "projection": "rectangular"
            },
            "topicDetails": {
                "topicCategories": [
                    "https://en.wikipedia.org/wiki/Entertainment",
                    "https://en.wikipedia.org/wiki/Film"
                ]
            }
        }
    ],
    "nextPageToken": "CAUQAA",
    "pageInfo": {
        "totalResults": 75,
        "resultsPerPage": 5
    }
}

SOURCE = 'YT'

class GetVideoTest(TestCase):
    def setUp(self):
        for vid in dict_vids["items"]:
            id = vid['id']
            title = vid['snippet']['title']
            duration = parse_duration(vid['contentDetails']['duration'])
            description = vid['snippet']['description']
            pub_time = parse_datetime(vid['snippet']['publishedAt'])
            category = int(vid['snippet']['categoryId'])

            channel_title = vid['snippet']['channelTitle']
            channel_id = vid['snippet']['channelId']
            Video.objects.create(source=SOURCE, platform_id=id, title=title, \
                                 duration=duration, description=description, \
                                 pub_date=pub_time, category_id=category,\
                                 channel_id = channel_id,channel_title = channel_title)

    def test_get_all_videos(self):
        response = client.get(reverse('get_post_videos'))
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_video(self):
        v1 = Video.objects.all()[0]
        response = client.get(
            reverse('get_delete_update_video', kwargs={'id': v1.id}))
        video = Video.objects.get(id=v1.id)
        serializer = VideoSerializer(video)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_video(self):
        response = client.get(
            reverse('get_delete_update_video', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




