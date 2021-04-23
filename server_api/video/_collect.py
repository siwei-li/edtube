# _collect.py created by sylvi at 2021/2/21 5:28 PM
from django.utils.dateparse import parse_datetime, parse_duration
from video.models import Video

dict = {
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

for vid in dict["items"][1:]:
    id = vid['id']
    title = vid['snippet']['title']
    duration = parse_duration(vid['contentDetails']['duration'])
    description = vid['snippet']['description']
    pub_time = parse_datetime(vid['snippet']['publishedAt'])
    category = int(vid['snippet']['categoryId'])
    Video.objects.create(source=SOURCE, platform_id=id, title=title, \
                         duration=duration, description=description, \
                         pub_date=pub_time, category_id=category)

for vid in dict["items"]:
    id = vid['id']
    channel_title = vid['snippet']['channelTitle']
    channel_id = vid['snippet']['channelId']
    # print(channel_title)
    video = Video.objects.get(platform_id=id)
    # print(video)
    video.channel_id = channel_id
    video.channel_title = channel_title
    video.save(update_fields=['channel_id','channel_title'])

# ==========================================
cats = {
    "kind": "youtube#videoCategoryListResponse",
    "etag": "7Omb5EYJ5gb2tL6k84F-F3tduKI",
    "items": [
        {
            "kind": "youtube#videoCategory",
            "etag": "grPOPYEUUZN3ltuDUGEWlrTR90U",
            "id": "1",
            "snippet": {
                "title": "Film & Animation",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Q0xgUf8BFM8rW3W0R9wNq809xyA",
            "id": "2",
            "snippet": {
                "title": "Autos & Vehicles",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "qnpwjh5QlWM5hrnZCvHisquztC4",
            "id": "10",
            "snippet": {
                "title": "Music",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "HyFIixS5BZaoBdkQdLzPdoXWipg",
            "id": "15",
            "snippet": {
                "title": "Pets & Animals",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "PNU8SwXhjsF90fmkilVohofOi4I",
            "id": "17",
            "snippet": {
                "title": "Sports",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "5kFljz9YJ4lEgSfVwHWi5kTAwAs",
            "id": "18",
            "snippet": {
                "title": "Short Movies",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "ANnLQyzEA_9m3bMyJXMhKTCOiyg",
            "id": "19",
            "snippet": {
                "title": "Travel & Events",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "0Hh6gbZ9zWjnV3sfdZjKB5LQr6E",
            "id": "20",
            "snippet": {
                "title": "Gaming",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "q8Cp4pUfCD8Fuh8VJ_yl5cBCVNw",
            "id": "21",
            "snippet": {
                "title": "Videoblogging",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "cHDaaqPDZsJT1FPr1-MwtyIhR28",
            "id": "22",
            "snippet": {
                "title": "People & Blogs",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "3Uz364xBbKY50a2s0XQlv-gXJds",
            "id": "23",
            "snippet": {
                "title": "Comedy",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "0srcLUqQzO7-NGLF7QnhdVzJQmY",
            "id": "24",
            "snippet": {
                "title": "Entertainment",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "bQlQMjmYX7DyFkX4w3kT0osJyIc",
            "id": "25",
            "snippet": {
                "title": "News & Politics",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Y06N41HP_WlZmeREZvkGF0HW5pg",
            "id": "26",
            "snippet": {
                "title": "Howto & Style",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "yBaNkLx4sX9NcDmFgAmxQcV4Y30",
            "id": "27",
            "snippet": {
                "title": "Education",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Mxy3A-SkmnR7MhJDZRS4DuAIbQA",
            "id": "28",
            "snippet": {
                "title": "Science & Technology",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "p3lEirEJApyEkuWpaGEHoF-m-aA",
            "id": "29",
            "snippet": {
                "title": "Nonprofits & Activism",
                "assignable": True,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "4pIHL_AdN2kO7btAGAP1TvPucNk",
            "id": "30",
            "snippet": {
                "title": "Movies",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Iqol1myDwh2AuOnxjtn2AfYwJTU",
            "id": "31",
            "snippet": {
                "title": "Anime/Animation",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "tzhBKCBcYWZLPai5INY4id91ss8",
            "id": "32",
            "snippet": {
                "title": "Action/Adventure",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "ii8nBGYpKyl6FyzP3cmBCevdrbs",
            "id": "33",
            "snippet": {
                "title": "Classics",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Y0u9UAQCCGp60G11Arac5Mp46z4",
            "id": "34",
            "snippet": {
                "title": "Comedy",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "_YDnyT205AMuX8etu8loOiQjbD4",
            "id": "35",
            "snippet": {
                "title": "Documentary",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "eAl2b-uqIGRDgnlMa0EsGZjXmWg",
            "id": "36",
            "snippet": {
                "title": "Drama",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "HDAW2HFOt3SqeDI00X-eL7OELfY",
            "id": "37",
            "snippet": {
                "title": "Family",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "QHiWh3niw5hjDrim85M8IGF45eE",
            "id": "38",
            "snippet": {
                "title": "Foreign",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "ztKcSS7GpH9uEyZk9nQCdNujvGg",
            "id": "39",
            "snippet": {
                "title": "Horror",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "Ids1sm8QFeSo_cDlpcUNrnEBYWA",
            "id": "40",
            "snippet": {
                "title": "Sci-Fi/Fantasy",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "qhfgS7MzzZHIy_UZ1dlawl1GbnY",
            "id": "41",
            "snippet": {
                "title": "Thriller",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "TxVSfGoUyT7CJ7h7ebjg4vhIt6g",
            "id": "42",
            "snippet": {
                "title": "Shorts",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "o9w6eNqzjHPnNbKDujnQd8pklXM",
            "id": "43",
            "snippet": {
                "title": "Shows",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        },
        {
            "kind": "youtube#videoCategory",
            "etag": "mLdyKd0VgXKDI6GevTLBAcvRlIU",
            "id": "44",
            "snippet": {
                "title": "Trailers",
                "assignable": False,
                "channelId": "UCBR8-60-B28hp2BmDPdntcQ"
            }
        }
    ]
}

'''
{
  "kind": "youtube#videoListResponse",
  "etag": "Tu2YnC-p9T6eDF75HcI9V_WLeKY",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "Gq2WVi4pAZ3-OV1jN-akP41D5ak",
      "id": "fwQci1cRiFU",
      "contentDetails": {
        "duration": "PT11M30S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "6oMf6iQ6_GsuQJglyvyB6cDsXlM",
      "id": "LZie2QC5Jbc",
      "contentDetails": {
        "duration": "PT21M46S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "YnaRSAXvDjRrh8dkL326B4iNzZo",
      "id": "WJownYnZ1ZQ",
      "contentDetails": {
        "duration": "PT25M7S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "9hhu4Q2sWkXZ8haC6UKPIja0R_g",
      "id": "l5XJdHfPc5o",
      "contentDetails": {
        "duration": "PT9M47S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "XqQUYZpFFQgIeg3p-MeuU7cwp5I",
      "id": "DivuT0HpazQ",
      "contentDetails": {
        "duration": "PT5M42S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "eqVDyI1aew6OW0IaFRLUtzs2X9E",
      "id": "vv6GcsLxMiQ",
      "contentDetails": {
        "duration": "PT18M4S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "KUwR9Jqkw_f8iU0XV2c0ionLBv0",
      "id": "0Rfushlee0U",
      "contentDetails": {
        "duration": "PT5M10S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "vAqOnRjBXQtPaGLZuIn53_bIJ3g",
      "id": "kpa_HO6yy18",
      "contentDetails": {
        "duration": "PT4M2S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "zsfNWjpmjKAyYQcJrrutojjQxJ4",
      "id": "DsUWFVKJwBM",
      "contentDetails": {
        "duration": "PT3M3S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "PbTd4mdGV6_Bylob8-Arh89fXf8",
      "id": "PYGeap5AGUU",
      "contentDetails": {
        "duration": "PT7M4S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "Z_7uvT2uNmO3NrSs4F_sTDVQj_E",
      "id": "5o1KYoXO6l4",
      "contentDetails": {
        "duration": "PT15M21S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "gluRT9ECf3PA75EgMYBmwzAVH6I",
      "id": "CfW845LNObM",
      "contentDetails": {
        "duration": "PT16M23S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "5_xH_jjNWU2E_LUhsn9eAndd3VU",
      "id": "3d6DsjIBzJ4",
      "contentDetails": {
        "duration": "PT22M20S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "zltrrJpfLVtFSyeejYKOugv-nHs",
      "id": "f3cEzlElVrw",
      "contentDetails": {
        "duration": "PT1H21M45S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "4Sj6FDVmLEQQgeBJQ25uUOQZzQk",
      "id": "_deujLjHAk0",
      "contentDetails": {
        "duration": "PT20M54S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "GovJsPwyU4jvYC2Sz5XYJ4FspIY",
      "id": "t9ETY25xQAI",
      "contentDetails": {
        "duration": "PT9M54S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "NtxSO0e1d3epCGnotJBdlyfKGlw",
      "id": "rEBiSYTY2PI",
      "contentDetails": {
        "duration": "PT10M59S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "Gk6PDJG29_Uc6X3EvQExPrIkE9I",
      "id": "DgfyryZJES4",
      "contentDetails": {
        "duration": "PT18M",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "zIEyaAbnbW4MHoJD0lyyjMVKk44",
      "id": "9Nx09pigZRI",
      "contentDetails": {
        "duration": "PT52M25S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "MuQoLiF40SZLgjh5R5i4U5rasT0",
      "id": "5YLDStBmJyM",
      "contentDetails": {
        "duration": "PT14M53S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "THIPQvNldTeLOVPng0Fk2MChc-Y",
      "id": "8yLSkmrUhcg",
      "contentDetails": {
        "duration": "PT34M54S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "OWkDNMGduLt03zVP1V2QtwpR-Wg",
      "id": "rL0_vOw6eCc",
      "contentDetails": {
        "duration": "PT19M19S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "aKDApI9bQx31t-dvp_lwObkxzTY",
      "id": "uxthZLy0Ftk",
      "contentDetails": {
        "duration": "PT6M48S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "bo8lrJHx5Q4Xbpaf8z0Nv5K_tpI",
      "id": "RPDBcdDGrnE",
      "contentDetails": {
        "duration": "PT27M27S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "wyt-FY6ywUkXSR93pej96urKsgQ",
      "id": "4MmSZrAlqKc",
      "contentDetails": {
        "duration": "PT13M49S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "JfwCIZtyDFofBkKsfoNc1vzavBo",
      "id": "pNp8Qf20-sA",
      "contentDetails": {
        "duration": "PT7M29S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "PFiwK3F94dy5m0N0pYn9Ey1ZRmE",
      "id": "Spq-xDDsEo4",
      "contentDetails": {
        "duration": "PT30M21S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "7_oJ8xssgMbyOVBQkIhwYYdnlpo",
      "id": "fo-alw2q-BU",
      "contentDetails": {
        "duration": "PT8M40S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "lvUDfniMxfeTOJT9-l3tPW9a3NM",
      "id": "HbgzrKJvDRw",
      "contentDetails": {
        "duration": "PT16M",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "eDSPBrIIIbUmf4EqZvBFIA0jzvM",
      "id": "EMHtNNP6s0A",
      "contentDetails": {
        "duration": "PT1M47S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "jznmA2Lsd23NjF04gZhyBFqHzRE",
      "id": "y2ikvX9UB-Q",
      "contentDetails": {
        "duration": "PT15M23S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "pCFtM-3sGbDLdBIgm6v2QNretik",
      "id": "kpz_U8wHpa8",
      "contentDetails": {
        "duration": "PT19M38S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "G0rfm4hd5tD8yCO5KXrAAUgdm2M",
      "id": "JauII1jCG6Q",
      "contentDetails": {
        "duration": "PT38M48S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "WIfLkxVgANxPPyMDQOXiLyELhVE",
      "id": "p7bzE1E5PMY",
      "contentDetails": {
        "duration": "PT14M34S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "jWUv278CZeV4pi8D6HSZMDgW3TA",
      "id": "Hy1hE0HBR3U",
      "contentDetails": {
        "duration": "PT57M30S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "biFjWYGXlM5kO2lNTB4N11UgZ5A",
      "id": "lRdFl5E-D0M",
      "contentDetails": {
        "duration": "PT9M37S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "-GwuIyzkwq1jj7Er10l1Vbs_VGA",
      "id": "UibfDUPJAEU",
      "contentDetails": {
        "duration": "PT24M13S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "c6UCpIgMWiB8c6U2Qpn4HIXydZw",
      "id": "O6txOvK-mAk",
      "contentDetails": {
        "duration": "PT5M44S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "YSf7CDYvDLpBC0eRDfwg6ymDfEA",
      "id": "1OE1TmSvpF4",
      "contentDetails": {
        "duration": "PT8M52S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "NqXvXXRegvWfLr8PgEXLoPM-F58",
      "id": "2lfA7-s8p94",
      "contentDetails": {
        "duration": "PT6M48S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "cO6gTX7eRtn8DHbRuPTOmBYbSzY",
      "id": "c3mwVaQIZ1c",
      "contentDetails": {
        "duration": "PT4M47S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": True,
        "regionRestriction": {
          "blocked": [
            "GL",
            "IO",
            "KP",
            "PR",
            "SS",
            "UM"
          ]
        },
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "BvT1-ixY5sIhzEaRs88PF8xchXE",
      "id": "Vd-Izm9kfnY",
      "contentDetails": {
        "duration": "PT15M15S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "TjXCE_7lH6RhyAvNYS17J_ZicnQ",
      "id": "1ystN_hz5l0",
      "contentDetails": {
        "duration": "PT57M12S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "9s1a1Yc7pS1nBpFLFrKK9OW5uTA",
      "id": "ABm7nMVyNh4",
      "contentDetails": {
        "duration": "PT5M36S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "wPNmqAQ9Ddi2HNisDpiIBrf3nPw",
      "id": "Y0l9wVILwI8",
      "contentDetails": {
        "duration": "PT25M31S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "V3PjJMwE5-bthSt12w8-ckfJluE",
      "id": "bhyzk6Ty-Ms",
      "contentDetails": {
        "duration": "PT9M26S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "regionRestriction": {
          "blocked": [
            "BE",
            "CA",
            "CH",
            "FR"
          ]
        },
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "xqNchFsAX9jpJtX8-_HIZzO--N0",
      "id": "ihzaYhGhJ2E",
      "contentDetails": {
        "duration": "PT8M1S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "3SQRTymiWVGifOaCjLlG6LDCJTs",
      "id": "KOL8gpqIbtM",
      "contentDetails": {
        "duration": "PT5M28S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "9JMGQt_H8UaLyBG4RfIx2BLISw0",
      "id": "SwQhKFMxmDY",
      "contentDetails": {
        "duration": "PT2H12M42S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    }
  ],
  "nextPageToken": "CDIQAA",
  "pageInfo": {
    "totalResults": 75,
    "resultsPerPage": 50
  }
}

{
  "kind": "youtube#videoListResponse",
  "etag": "2rLS45dvrGAXPmyw_4dVdIuo558",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "qnWuOzC4rZHmuoEM_cAU1d1Cn8U",
      "id": "jjhC80M4ScE",
      "contentDetails": {
        "duration": "PT15M52S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "UH54OLzuY2w_gM0qNmOUqT--xkE",
      "id": "HoP4lK1drrA",
      "contentDetails": {
        "duration": "PT10M54S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "1DREr1EkfUHW6y3TRrhBGwlQK-s",
      "id": "r6YCSeeMN4I",
      "contentDetails": {
        "duration": "PT5M55S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "XaI7B4pBhxD2GKwAwhA8m7hmhrA",
      "id": "9tABgYM0Gsw",
      "contentDetails": {
        "duration": "PT1H42M44S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "65a7eLdU541l21GiG2469YRHgx8",
      "id": "W748SgX8s0k",
      "contentDetails": {
        "duration": "PT14M56S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "Y9yXdrkHLXbMmuLVjO31ayN4yTw",
      "id": "WWeWmjlnB9c",
      "contentDetails": {
        "duration": "PT3M25S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "47EPyh4lJmMueeKj_aT9qIwvyQA",
      "id": "h3xEHigWShM",
      "contentDetails": {
        "duration": "PT2M50S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "URFKEPzfziIlbM_o49zC7QvxHpE",
      "id": "HlfGJnBuD4o",
      "contentDetails": {
        "duration": "PT8M37S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "u90UkdHhkhVyMwYfPXETBazLrhg",
      "id": "CTE08SS8fNk",
      "contentDetails": {
        "duration": "PT36M31S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "1T0vdA0nOT1fY5WnEjL1KwmHeTA",
      "id": "x56SFU5k8zE",
      "contentDetails": {
        "duration": "PT7M30S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "7D9JB0d0FGmkGiUmspDUa6BUOFQ",
      "id": "IzTdpTHIgkc",
      "contentDetails": {
        "duration": "PT58M40S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "-AMp06tKlUldW-X6md32HfTbSPg",
      "id": "fgejrdIsQSQ",
      "contentDetails": {
        "duration": "PT6M49S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "YdHpDeMrZgBuEgoYrLWriXJuGV4",
      "id": "zDuJxcD4K7c",
      "contentDetails": {
        "duration": "PT3M50S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "KRm2KyYCJ5P0gsXcs93MiOC0klI",
      "id": "14dwegqniNg",
      "contentDetails": {
        "duration": "PT1H28M50S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": False,
        "regionRestriction": {
          "blocked": [
            "CU",
            "IR",
            "KP",
            "SY"
          ]
        },
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "-Juec3dmg_vUNhgBEpmSzavLPJ0",
      "id": "VFns39RXPrU",
      "contentDetails": {
        "duration": "PT24M16S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "r2sTzUB1koBeKwOynVmKgDFdAsg",
      "id": "HdnC_KE7hYY",
      "contentDetails": {
        "duration": "PT12M15S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "yLxAEg8O2oXKzc_87OUP8McTp6I",
      "id": "PAAeSTuwlvE",
      "contentDetails": {
        "duration": "PT10M47S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "rtBOq13bZZFw0Yldh7n6rpu6jQs",
      "id": "D-x1vIxi7dU",
      "contentDetails": {
        "duration": "PT13M53S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "sBE4DeD1Pd5EO_XrkCCIif12t6A",
      "id": "iyJ6ZsAuT-M",
      "contentDetails": {
        "duration": "PT54M48S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "zgY5B_2xWInnnOFb071D-jZxT2I",
      "id": "Rs572Cf4zkk",
      "contentDetails": {
        "duration": "PT9M47S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "6hkXfsAscBoaG0wavEUrnpYSD_0",
      "id": "XKu_SEDAykw",
      "contentDetails": {
        "duration": "PT24M2S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "h1pp3WqI9c-wne9qBhfm7G3hKEE",
      "id": "D919764d18M",
      "contentDetails": {
        "duration": "PT6M46S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "True",
        "licensedContent": True,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "D_Keeq-hNpOs9TCj1iCSVroh9jw",
      "id": "VgQJvNhuiAE",
      "contentDetails": {
        "duration": "PT2M10S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "tIxPXV7f3gUMD50zP0IRnBRNcVI",
      "id": "dke8K8GnsMo",
      "contentDetails": {
        "duration": "PT28M57S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "True",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    },
    {
      "kind": "youtube#video",
      "etag": "u-3H3lenAsD3YIKR9SHqj0ohYbs",
      "id": "WlJGloEHRIA",
      "contentDetails": {
        "duration": "PT15M1S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "False",
        "licensedContent": False,
        "contentRating": {},
        "projection": "rectangular"
      }
    }
  ],
  "prevPageToken": "CDIQAQ",
  "pageInfo": {
    "totalResults": 75,
    "resultsPerPage": 50
  }
}
'''
