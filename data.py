# -*- coding: utf-8 -*-
# Single source of truth. Edit here, re-run build.py, and every page updates.

SKILL_GROUPS = [
    ("Design & Prototyping", [
        ("solidworks", "SolidWorks"),
        ("drawings", "Engineering Drawings"),
        ("printing", "3D Printing"),
        ("pcb", "PCB Design"),
        ("microfluidics", "Microfluidics"),
        ("prototyping", "Prototyping"),
        ("dfm", "DFM"),
    ]),
    ("Testing & Product Development", [
        ("benchtop", "Benchtop Testing"),
        ("calibration", "Sensor Calibration"),
        ("daq", "Data Acquisition"),
        ("validation", "Design Validation"),
        ("optimization", "Design Optimization"),
        ("expdesign", "Experimental Design"),
    ]),
    ("Programming & Data Analysis", [
        ("python", "Python"),
        ("matlab", "MATLAB"),
        ("arduino", "Arduino"),
        ("stats", "Statistical Analysis"),
        ("ml", "Machine Learning"),
        ("dataanalysis", "Data Analysis"),
    ]),
    ("Quality & Regulatory", [
        ("capa", "CAPA"),
        ("rca", "Root Cause Analysis"),
        ("controls", "FDA Design Controls"),
        ("sop", "SOP Development"),
        ("regcompliance", "Regulatory Compliance"),
    ]),
    ("Leadership & Communication", [
        ("leadership", "Team Leadership"),
        ("xfn", "Cross-Functional Collaboration"),
        ("presenting", "Technical Presentations"),
        ("mentoring", "Mentoring & Program Development"),
        ("techcomm", "Technical Communication"),
        ("documentation", "Engineering Documentation"),
        ("techwriting", "Technical Writing"),
    ]),
]

# skills demonstrated in the Leadership section (not a filterable project);
# a chip for one of these with no project of its own links to #leadership
LEAD_SKILLS = ["leadership", "xfn", "mentoring"]

SKILL_NAMES = {k: v for _, pairs in SKILL_GROUPS for k, v in pairs}

PROJECTS = [
    {
        "slug": "applied-medical",
        "industry": True,
        "title": "Quality engineering in a regulated device plant",
        "short": "Applied Medical",
        "org": "Applied Medical",
        "role": "Quality Systems Engineer Intern",
        "dates": "June 2026 \u2013 Present",
        "sort": "2026-06",
        "kind": "Internship",
        "summary": "Leading two CAPA investigations end to end, and redesigning a peel-test fixture "
                   "so package seal-strength results stop drifting between operators.",
        "skills": ["solidworks", "drawings", "validation", "capa", "rca", "xfn", "presenting", "techcomm"],
        "context": "Applied Medical builds surgical devices under ISO 13485 and 21 CFR Part 820. "
                   "Quality engineering is where a suspected problem becomes a documented decision: "
                   "you have to show what went wrong, why, and what evidence says the fix worked.",
        "did": [
            "Perform risk assessments and write the technical justifications for opening Corrective "
            "and Preventive Actions, against ISO 13485 and 21 CFR Part 820.",
            "Lead two CAPA investigations through document review, root cause analysis, and "
            "cross-functional process evaluation, then present findings and corrective-action "
            "recommendations to senior management.",
            "Redesign a package peel-test fixture in SolidWorks, produce the engineering drawings, "
            "and fabricate and validate the design to make FFS package seal-strength testing more "
            "consistent and repeatable.",
        ],
        "next": "Ask me about: how you decide a root cause is actually the root cause.",
    },
    {
        "slug": "petalgrip",
        "title": "PetalGrip \u2014 redesigned cervical biopsy forceps",
        "short": "PetalGrip",
        "org": "Cervical biopsy forceps",
        "role": "Design Engineer",
        "dates": "April 2026 \u2013 June 2026",
        "sort": "2026-04",
        "kind": "Design project",
        "summary": "Redesigned cervical biopsy forceps through CAD, prototyping, simulation, "
                   "and testing, and documented the design decisions, materials, manufacturing "
                   "considerations, test results, and cost analysis in a comprehensive "
                   "engineering report.",
        "skills": ["solidworks", "prototyping", "optimization", "documentation", "dfm"],
        "context": "Cervical biopsy forceps have changed very little in decades, and the "
                   "existing designs ask a lot of the clinician's hand. The brief was to rethink "
                   "the jaw and handle geometry without making the device harder to manufacture.",
        "did": [
            "Develop the forceps concept in SolidWorks \u2014 part models, assemblies, and detailed "
            "engineering drawings built for rapid prototyping.",
            "Run iterative design optimisation through SolidWorks simulation, prototype testing, "
            "and performance evaluation, improving functionality, manufacturability, and ergonomics.",
            "Author the engineering design report covering design rationale, prototyping method, "
            "test results, material selection, manufacturing considerations, and cost analysis.",
        ],
        "next": "Ask me about: the trade-off between jaw closing force and handle travel.",
    },
    {
        "slug": "laparoscopic-trainer",
        "title": "Turning a benchtop test rig into a teaching lab",
        "short": "Laparoscopic Trainer Lab Module",
        "org": "UCI \u00d7 Applied Medical",
        "role": "Team Lead",
        "dates": "January 2026 \u2013 June 2026",
        "sort": "2026-01",
        "kind": "Collaboration",
        "summary": "Created a biomedical engineering lab module that teaches experimental design "
                   "and regulatory compliance through hands-on device testing, using laparoscopic "
                   "trainers to assess performance against ISO 7741, and published the work in a "
                   "conference paper.",
        "skills": ["expdesign", "benchtop", "regcompliance", "dataanalysis", "techwriting"],
        "context": "A test protocol is only useful if someone else can repeat it. This project "
                   "started as force measurement on laparoscopic instruments and ended as an "
                   "ABET-accredited teaching module \u2014 which meant every step had to survive "
                   "being handed to a student who had never seen the rig.",
        "did": [
            "Design and run benchtop testing protocols quantifying laparoscopic tool\u2013tissue "
            "interaction forces, using Arduino-based data acquisition.",
            "Apply ISO 7741 and FDA 510(k) design-control principles to evaluate device "
            "performance and safety margins.",
            "Co-author a published ASEE conference paper, and write the SOPs, instructional "
            "materials, and quantitative analyses for an ABET-accredited biomedical engineering "
            "laboratory course.",
        ],
        "next": "Ask me about: what breaks when you hand your protocol to a stranger.",
    },
    {
        "slug": "suture-sensor",
        "title": "A pressure sensor built to a spec, then proven against it",
        "short": "Novel Suture Project",
        "org": "Novel Suture Project",
        "role": "Fabrication Lead",
        "dates": "May 2025 \u2013 Present",
        "sort": "2025-05",
        "kind": "Hardware",
        "summary": "Custom PCB pressure sensor for biomedical force monitoring \u2014 0\u2013183 kPa, "
                   "R\u00b2 = 0.997, 0.20 kPa resolution, 26.5 dB SNR.",
        "skills": ["pcb", "calibration", "daq", "matlab", "sop", "presenting"],
        "context": "Building the sensor was the easy half. The harder half was characterising it "
                   "honestly: resolution, repeatability, signal-to-noise, and residual error, "
                   "documented well enough that someone else could trust the numbers.",
        "did": [
            "Build and calibrate a custom PCB-based pressure sensor for biomedical force "
            "monitoring \u2014 0\u2013183 kPa range, R\u00b2 = 0.997, 0.046% residual error.",
            "Run hardware validation in MATLAB, reaching 0.20 kPa resolution and 26.5 dB SNR, "
            "while evaluating repeatability, accuracy, and process performance.",
            "Write and implement the SOPs for fabrication, testing, and design verification "
            "under quality control standards.",
            "Present at the 2025 National BMES Conference and the UCI Undergraduate Research "
            "Opportunities Program Symposium.",
        ],
        "next": "Ask me about: why 26.5 dB was the number that mattered.",
    },
    {
        "slug": "downing-lab",
        "title": "What happens to a cell's scaffolding when you switch off CSRP1",
        "short": "Downing Lab",
        "org": "UC Irvine",
        "role": "Data Analytics Lead",
        "dates": "April 2025 \u2013 Present",
        "sort": "2025-04",
        "kind": "Research",
        "summary": "Quantified cytoskeletal disruption in lung cancer cells after CSRP1 knockdown "
                   "across 20+ morphology parameters \u2014 actin disorganisation at p < 0.0001.",
        "skills": ["python", "stats", "presenting"],
        "context": "Immunofluorescence images are easy to look at and hard to measure. Most of "
                   "this work was building the measurement layer \u2014 turning a folder of images "
                   "into numbers that hold up to a statistical test.",
        "did": [
            "Investigate cytoskeletal changes in lung cancer cell lines after CSRP1 knockdown "
            "using immunofluorescence staining and quantitative analysis, measuring 20+ cell "
            "morphology parameters in ImageJ, Python, and R.",
            "Develop a Python distance-analysis pipeline to quantify spatial relationships "
            "between cellular structures from immunofluorescence imaging data.",
            "Present findings showing statistically significant disruption of actin organisation "
            "(p < 0.0001) following CSRP1 knockdown, at the 2025 National BMES Conference.",
        ],
        "next": "Ask me about: choosing which 20 morphology parameters are worth measuring.",
    },
    {
        "slug": "ultrascan-pro",
        "title": "UltraScan Pro — an Arduino ultrasonic imaging system",
        "short": "UltraScan Pro",
        "org": "Arduino ultrasonic imaging",
        "role": "Team Leader",
        "dates": "September 2025 – December 2025",
        "sort": "2025-09",
        "kind": "Team project",
        "summary": "A simplified ultrasound-style ranging system — ultrasonic sensing, a servo "
                   "sweep, and real-time MATLAB visualisation building a 180° map of nearby "
                   "objects. Placed 2nd of 19 teams.",
        "skills": ["matlab", "arduino", "leadership"],
        "context": "The goal was to reproduce the core idea of ultrasound imaging — sweep a "
                   "beam, time the echoes, build a picture — with hobby hardware, and to lead a "
                   "four-person team through it on a fixed deadline.",
        "did": [
            "Direct a 4-member engineering team to design and prototype a simplified "
            "ultrasound-style ranging system.",
            "Integrate ultrasonic sensors, servo motor control, an LCD interface, and real-time "
            "MATLAB visualisation to generate a 180° spatial map of surrounding objects.",
            "Develop interactive feedback features — LED indicators and motion alerts — "
            "to make the output easier to read and interpret.",
            "Deliver a final solution that placed 2nd out of 19 teams.",
        ],
        "next": "Ask me about: what limits the angular resolution of a servo-swept sensor.",
    },
    {
        "slug": "preeclampsia-ml",
        "title": "Predicting preeclampsia risk from clinical parameters",
        "short": "Preeclampsia Risk Prediction",
        "org": "Preeclampsia Risk Prediction",
        "role": "MATLAB machine-learning pipeline",
        "dates": "September 2025 – December 2025",
        "sort": "2025-09",
        "kind": "Course project",
        "summary": "A reproducible MATLAB workflow predicting preeclampsia risk — three models "
                   "(random forest, gradient boosting, SVM) preprocessed, tuned, and compared on a "
                   "clinical dataset.",
        "skills": ["matlab", "stats", "ml"],
        "context": "Clinical risk prediction is only useful if the pipeline behind it is honest "
                   "and repeatable. The work was less about any one model and more about building "
                   "a workflow whose numbers could be trusted and rerun.",
        "did": [
            "Build a machine-learning analysis workflow in MATLAB to predict preeclampsia risk "
            "from a clinical parameter dataset.",
            "Preprocess data, normalise features, and engineer inputs for three models — "
            "random forest, gradient boosting, and SVM — to compare predictive performance.",
            "Optimise the models, compare accuracy metrics, and document results to support "
            "data-driven clinical decision applications.",
            "Produce a reproducible, validated pipeline used for class demonstration and "
            "technical reporting.",
        ],
        "next": "Ask me about: why model choice mattered less than the preprocessing here.",
    },
    {
        "slug": "starchip",
        "title": "StarChip — a low-cost microfluidic fluorescence reader",
        "short": "StarChip",
        "org": "Microfluidic diagnostics",
        "role": "Electrical Software & Testing Lead",
        "dates": "January 2025 – March 2025",
        "sort": "2025-01",
        "kind": "Team project",
        "summary": "A low-cost microfluidic device for rapid fluorescence quantification in "
                   "biomedical assays, with Arduino-based control and sensing and an OLED readout.",
        "skills": ["printing", "microfluidics", "arduino", "leadership"],
        "context": "Fluorescence readers are expensive. StarChip was an attempt to hit a usable "
                   "signal at a fraction of the cost, using laser-cut and 3D-printed parts, PDMS "
                   "channels, and off-the-shelf electronics.",
        "did": [
            "Develop a low-cost microfluidic device for rapid, efficient fluorescence "
            "quantification in biomedical assays.",
            "Program Arduino-based control and sensing systems with an integrated OLED display "
            "for real-time data visualisation and signal optimisation.",
            "Fabricate device components using laser cutting, 3D printing, and "
            "polydimethylsiloxane (PDMS).",
            "Run functional testing and analysis to develop a scalable, low-cost biomedical "
            "diagnostic prototype.",
        ],
        "next": "Ask me about: where the noise floor sat once the cost was stripped out.",
    },
    {
        "slug": "seraswaddle",
        "title": "SeraSwaddle — a neonatal hypothermia device pitch",
        "short": "SeraSwaddle",
        "org": "OPEN MIC Medical Innovation Competition",
        "role": "2nd place — Mechanical/Electrical track",
        "dates": "March 2025",
        "sort": "2025-03",
        "kind": "Competition",
        "summary": "Pitched SeraSwaddle, a neonatal hypothermia treatment device — 2nd in the "
                   "Mechanical/Electrical track, with a business plan, design specs, and a "
                   "510(k)-aligned risk strategy.",
        "skills": ["controls", "presenting"],
        "context": "OPEN MIC asks for a real unmet need and a credible route to a device. Neonatal "
                   "hypothermia is a large, under-addressed problem in low-resource settings, and "
                   "the pitch had to hold up on both the clinical and the regulatory side.",
        "did": [
            "Pitch SeraSwaddle, a neonatal hypothermia treatment device, and secure 2nd place in "
            "the Mechanical/Electrical track.",
            "Develop the startup business plan and outline device design specifications.",
            "Define a risk mitigation strategy aligned with the FDA 510(k) process.",
        ],
        "next": "Ask me about: what makes neonatal hypothermia a device problem and not just a "
                "supply problem.",
    },
    {
        "slug": "rc-rover",
        "title": "A remote-controlled rover, designed and tested end to end",
        "short": "Remote Controlled Rover",
        "org": "Remote Controlled Rover",
        "role": "Team Leader",
        "dates": "September 2024 – December 2024",
        "sort": "2024-09",
        "kind": "Team project",
        "summary": "Full mechanical design and test cycle of an RC rover — SolidWorks "
                   "assemblies and Ackermann steering geometry that improved steering performance "
                   "by 20%.",
        "skills": ["solidworks", "leadership"],
        "context": "First engineering team I led. The rover was the vehicle for learning how to "
                   "run a seven-person design cycle — from concept models to a rig you can "
                   "actually drive and measure.",
        "did": [
            "Direct a 7-member team through the full mechanical design and testing cycle of a "
            "remote-controlled rover.",
            "Model assemblies in SolidWorks and improve steering performance by 20% through "
            "Ackermann geometry optimisation and iterative testing.",
        ],
        "next": "Ask me about: how Ackermann geometry turns into a measurable 20%.",
    },
]
