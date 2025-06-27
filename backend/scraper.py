# Include finished scraper (being worked on by another team member)
import json

def scraper():
    # json data format
    data = {
        "Carlos Varela|RPI": {
            "papers": [
                {
                    "title": "Airplane Flight Safety Using Error-Tolerant Data Stream Processing",
                    "abstract": "Our current main research interest is the investigation of fundamental distributed computing and software engineering principles to enable intelligent data-driven aero-space systems. We are at a crossroads of significant new advances in distributed computing, big data analytics, flight sensor technologies, and machine learning. Such crossroads presents an unparalleled opportunity for smarter flight systems. In particular, we are interested in performing fundamental research leading to an Internet of Planes platform, providing pilots and autonomous vehicles with unprecedented levels of real-time collaborative situational awareness using edge computing on distributed sensor data. We are also interested in fundamental research on software development and verification techniques for data-driven (and thus, stochastic) flight systems. Particularly, we want to investigate the notion of safety envelopes, to formally capture the conditions under which data-driven flight systems (such as the distributed control system of a smart wing) are guaranteed to behave correctly. While the potential applications and increased level of capability and safety of next-generation flight are enormous, the research challenges are commensurate. We are interested in forming an interdisciplinary Center for Intelligent Flight Systems tackling key open problems in the following thrusts: cyber physical systems, concurrent programming, and distributed computing development. We expect fundamental research results in these directions to be also applicable to other vehicle networks (e.g., of self-driving cars), and to distributed data stream analytics in other domains (e.g., health informatics.) In the following sections, we will illustrate research directions we intend to pursue, along with prior research experience and key results in each of these thrusts.",
                    # other fields?                    
                    "url": "http://wcl.cs.rpi.edu/papers/pilots-aesm.pdf",
                    "year": 2017,
                }
            ]
        }
    }
    
    # write the json data to a file (is there a better place to put this?)
    with open("professors.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    scraper()