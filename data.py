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
        ("meddevice", "Medical Device Design"),
        ("lasercutting", "Laser Cutting"),
        ("pdms", "PDMS Fabrication"),
    ]),
    ("Testing & Product Development", [
        ("benchtop", "Benchtop Testing"),
        ("calibration", "Sensor Calibration"),
        ("daq", "Data Acquisition"),
        ("validation", "Design Validation"),
        ("optimization", "Design Optimization"),
        ("expdesign", "Experimental Design"),
        ("testing", "Testing"),
    ]),
    ("Programming & Data Analysis", [
        ("python", "Python"),
        ("matlab", "MATLAB"),
        ("arduino", "Arduino"),
        ("stats", "Statistical Analysis"),
        ("ml", "Machine Learning"),
        ("dataanalysis", "Data Analysis"),
        ("dataviz", "Data Visualization"),
        ("datapreprocessing", "Data Preprocessing"),
        ("imageanalysis", "Image Analysis"),
    ]),
    ("Quality & Regulatory", [
        ("capa", "CAPA"),
        ("rca", "Root Cause Analysis"),
        ("controls", "FDA Design Controls"),
        ("sop", "SOP Development"),
        ("regcompliance", "Regulatory Compliance"),
        ("riskanalysis", "Risk Analysis"),
    ]),
    ("Leadership & Communication", [
        ("leadership", "Leadership"),
        ("xfn", "Cross-Functional Collaboration"),
        ("presenting", "Technical Presentations"),
        ("mentoring", "Mentoring & Program Development"),
        ("techcomm", "Technical Communication"),
        ("documentation", "Engineering Documentation"),
        ("techwriting", "Technical Writing"),
        ("scientificwriting", "Scientific Writing"),
        ("pitching", "Pitching"),
    ]),
    ("Business & Entrepreneurship", [
        ("entrepreneurship", "Entrepreneurship"),
        ("bizstrategy", "Business Strategy"),
        ("competitive", "Competitive Analysis"),
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
        "title": "Quality Engineering Internship at Applied Medical",
        "hide_role": True,
        "nav_label": "Applied Medical Internship",
        "hide_lede": True,
        "hero_image": "assets/applied-medical-detail-1.png",
        "aside_images": [
            "assets/applied-medical-detail-2.png",
            "assets/applied-medical-detail-3.png",
            "assets/applied-medical-detail-4.png",
        ],
        "short": "Applied Medical",
        "org": "Applied Medical",
        "role": "Quality Engineering Intern",
        "dates": "June 2026 \u2013 September 2026",
        "sort": "2026-06",
        "kind": "Internship",
        "summary": "Leading two CAPA investigations end to end, and redesigning a peel-test fixture "
                   "so package seal-strength results stop drifting between operators.",
        "skills": ["capa", "rca", "solidworks", "drawings", "competitive"],
        "background": [
            "Worked within Quality Systems in a regulated medical-device environment, with most "
            "of the internship focused on CAPA investigations.",
        ],
        "context": "Worked within Quality Systems in a regulated medical-device environment, with "
                   "most of the internship focused on CAPA investigations.",
        "did": [
            "Developed investigation plans for two cross-functional CAPAs, met with process "
            "owners and stakeholders, reviewed technical documentation, and evaluated evidence to "
            "determine likely root causes.",
            "Built an I-MR chart to evaluate failure frequency and process behavior, wrote CAPA "
            "investigation proposals, presented findings to senior leadership, and incorporated "
            "feedback into the investigation approach.",
            "Collaborated with another intern to redesign a package peel-test fixture in "
            "SolidWorks to better reflect real-world package opening; created engineering "
            "drawings and completed an initial prototype/testing round with the Packaging team.",
            "Supported Clinical Development by reviewing and verifying competitor claims across "
            "energy-device portfolios.",
            "Participated in weekly automation learning sessions covering PLCs, HMIs, ladder "
            "logic, robotics, and industrial controls.",
        ],
        "result": [
            "One CAPA was closed after the evidence supported a non-systemic issue, while the "
            "second progressed into corrective action after a procedural gap was identified.",
            "Developed a preliminary process-improvement plan for the second CAPA, outlining "
            "potential corrective steps for continued validation and implementation after the "
            "internship.",
            "Presented CAPA findings and peel-test fixture development to cross-functional "
            "stakeholders and senior leadership.",
            "Delivered a redesigned fixture concept, engineering drawings, and initial prototype "
            "for continued evaluation by the Packaging team.",
        ],
        "learnings": [
            "Learned to go beyond the documentation, speak with the people closest to the "
            "process, and follow the evidence even when it challenged the original assumption.",
            "Gained familiarity with ISO 13485 and 21 CFR Part 820 and how those requirements "
            "shape quality-system investigations and decision-making.",
            "Gained exposure to industrial controls, an area I had no prior background in and "
            "became interested in learning more about.",
        ],
"home_did": [
            "Led two cross-functional CAPA investigations under ISO 13485 and 21 CFR Part 820, "
            "using root cause analysis, process evaluation, and statistical monitoring to support "
            "closure of one CAPA and corrective action for another.",
            "Redesigned a package peel-test fixture in SolidWorks to better replicate real-world "
            "package opening, then created engineering drawings and tested an initial prototype "
            "for repeatability and usability.",
            "Supported Clinical Development by reviewing and verifying 70+ competitor claims for "
            "energy devices across manufacturer, clinical, and technical sources, organizing the "
            "findings into a structured comparison for internal use.",
        ],
        "next": "Ask me about: how you decide a root cause is actually the root cause.",
    },
    {
        "slug": "petalgrip",
        "title": "PetalGrip \u2014 redesigned cervical biopsy forceps",
        "short": "PetalGrip",
        "org": "UC Irvine",
        "role": "Design Engineer",
        "dates": "April 2026 \u2013 June 2026",
        "sort": "2026-04",
        "kind": "Design project",
        "hero_image": "assets/petalgrip-hero.png",
        "aside_images": [
            "assets/petalgrip-sim-detail.png",
            "assets/petalgrip-sim-detail-2.png",
            "assets/petalgrip-sim-detail-3.png",
        ],
        "summary": "Redesigned cervical biopsy forceps through CAD, prototyping, simulation, "
                   "and testing, and documented the design decisions, materials, manufacturing "
                   "considerations, test results, and cost analysis in a comprehensive "
                   "engineering report.",
        "skills": ["solidworks", "prototyping", "optimization", "documentation", "dfm"],
        "context": "Cervical biopsy forceps have changed very little in decades, and the "
                   "existing designs ask a lot of the clinician's hand. The brief was to rethink "
                   "the jaw and handle geometry without making the device harder to manufacture.",
        "background": [
            "SolidWorks course project focused on redesigning cervical biopsy forceps to "
            "improve tissue capture and retention.",
            "Cervical biopsies rely on high-quality tissue samples for pathological "
            "evaluation, making reliable specimen collection critical for early diagnosis.",
            "Existing forceps can lose tissue during withdrawal and produce variable biopsy "
            "depth, which can reduce sample quality and lead to repeat procedures.",
        ],
        "hide_lede": True,
        "did": [
            "Developed the forceps concept in SolidWorks, creating detailed part models, "
            "assemblies, and engineering drawings.",
            "Independently modeled a foldable net mechanism in SolidWorks to simulate the "
            "proposed tissue-retention design.",
            "Helped fabricate prototypes and iterated the design through simulation and "
            "functional testing.",
            "Documented the full design process through step-by-step CAD tutorials and a "
            "comprehensive engineering design report covering design rationale, prototyping, "
            "testing, materials, manufacturing, and cost analysis.",
        ],
        "challenges": [
            "Modeling a foldable net mechanism that could open, collapse, and fit within "
            "the forceps geometry.",
            "Determining how to securely integrate the net into the physical forceps "
            "prototype.",
        ],
        "outcomes": "Completed and submitted a final forceps prototype supported by a "
                    "comprehensive engineering design report.",
        "resources": [
            {
                "title": "Engineering Design Report",
                "thumb": "assets/petalgrip-report-thumb.png",
                "href": "assets/PetalGrip_Design_Report.pdf",
            },
            {
                "title": "CAD Tutorials",
                "thumb": "assets/petalgrip-cad-thumb.png",
                "links": [
                    {"label": "Parts", "href": "https://www.youtube.com/watch?v=vp34r5lha5o"},
                    {"label": "Assembly", "href": "https://www.youtube.com/watch?v=iFjUac2jj04"},
                ],
            },
            {
                "title": "Simulation and Motion Study",
                "thumb": "assets/petalgrip-sim-thumb.png",
                "href": "https://youtu.be/lUmuVqZAFyg",
            },
        ],
        "next": "Ask me about: the trade-off between jaw closing force and handle travel.",
    },
    {
        "slug": "laparoscopic-trainer",
        "title": "Laparoscopic Trainer Lab Module",
        "short": "Laparoscopic Trainer Lab Module",
        "org": "UCI \u00d7 Applied Medical",
        "role": "Team Lead",
        "dates": "January 2026 \u2013 June 2026",
        "sort": "2026-01",
        "kind": "Collaboration",
        "hero_image": "assets/laparoscopic-trainer-detail.png",
        "aside_images": [
            "assets/laparoscopic-trainer-detail-2.png",
            "assets/laparoscopic-trainer-detail-3.png",
        ],
        "summary": "Created a biomedical engineering lab module that teaches experimental design "
                   "and regulatory compliance through hands-on device testing, using laparoscopic "
                   "trainers to assess performance against ISO 7741, and published the work in "
                   "the American Society for Engineering Education (ASEE) conference paper.",
        "skills": ["expdesign", "benchtop", "regcompliance", "dataanalysis", "techwriting"],
        "hide_lede": True,
        "context": "A test protocol is only useful if someone else can repeat it. This project "
                   "started as force measurement on laparoscopic instruments and ended as an "
                   "ABET-accredited teaching module \u2014 which meant every step had to survive "
                   "being handed to a student who had never seen the rig.",
        "background": [
            "UCI lacked an undergraduate BME lab experience focused on regulatory compliance "
            "and the testing used to demonstrate that a medical device meets a standard.",
            "Developed a hands-on module for an ABET-accredited BME lab course to introduce "
            "students to experimental design, engineering testing, and regulatory evaluation.",
        ],
        "did": [
            "Designed and executed Arduino-based benchtop protocols to quantify laparoscopic "
            "tool\u2013tissue interaction forces and developed MATLAB analyses to interpret the "
            "resulting data.",
            "Created SOPs, instructional materials, and quantitative analyses for the lab module.",
            "Piloted the module with 20+ undergraduate students, tracking task-completion time "
            "and collecting survey feedback to identify usability issues and refine the lab "
            "experience before course implementation.",
            "Co-authored the conference paper documenting the module and its experimental and "
            "regulatory-testing framework.",
        ],
        "result": [
            "Refined the lab module through pilot testing and student feedback before "
            "classroom implementation.",
            "Confirmed that the laparoscopic trainers met the applicable ISO 7741 performance "
            "requirements through quantitative testing.",
            "Module planned for implementation in the BME laboratory course this academic year.",
            "Published the work in the American Society for Engineering Education (ASEE) conference paper.",
        ],
        "learnings": [
            "Reading and understanding technical standards well enough to apply them to testing.",
            "Learning how to turn a written standard into an actual test plan.",
            "Designing a lab that students with different levels of experience could follow.",
        ],
        "publication": {
            "label": "Published ASEE Conference Paper",
            "href": "https://peer.asee.org/work-in-progress-industry-driven-laboratory-module-using-laparoscopic-trainers-for-undergraduate-biomedical-engineering-education",
        },
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
        "summary": "Developing a novel suturing technique to address postpartum hemorrhage, "
                   "while leading development and optimization of the pressure-sensing system "
                   "used to test the design. Presented the work at the National BMES Conference "
                   "for two consecutive years.",
        "skills": ["matlab", "calibration", "benchtop", "techcomm", "leadership"],
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
        "summary": "Investigated how CSRP1 affects lung cancer cell structure, transitioning "
                   "from wet-lab research to quantitative image analysis and building Python "
                   "pipelines for cell morphology and lipid\u2013mitochondria colocalization. "
                   "Presented the work at National BMES for two consecutive years and "
                   "contributed to two manuscripts in preparation.",
        "skills": ["python", "imageanalysis", "stats", "dataviz", "scientificwriting"],
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
        "hero_image": "assets/ultrascan-pro-hero.png",
        "hide_lede": True,
        "resources_heading": "Project Outcomes",
        "resources_last": True,
        "aside_images": [
            "assets/ultrascan-pro-detail.png",
            "assets/ultrascan-pro-detail-2.png",
        ],
        "org": "Arduino ultrasonic imaging",
        "role": "Team Lead",
        "dates": "September 2025 – December 2025",
        "sort": "2025-09",
        "kind": "Team project",
        "summary": "Led a four-person team in building an Arduino-based ultrasonic scanning "
                   "system that converted sensor measurements into a real-time 180° spatial map "
                   "and earned 2nd place out of 19 teams.",
        "skills": ["arduino", "matlab", "daq", "dataviz", "leadership"],
        "context": "Arduino-based course project focused on microcontrollers, sensor "
                   "integration, and engineering design.",
        "background": [
            "Arduino-based course project focused on microcontrollers, sensor integration, "
            "and engineering design.",
            "Developed an ultrasonic scanning system with MATLAB visualization to map nearby "
            "objects in real time.",
        ],
        "did": [
            "Led a four-person team and coordinated integration across the ultrasonic sensor, "
            "servo motor, LCD interface, and MATLAB visualization.",
            "Coded the LCD interface, LED indicators, and motion-alert features.",
            "Coordinated subsystem testing and iteration as the team moved from individually "
            "functioning components to a fully integrated prototype.",
            "Helped troubleshoot a failed stepper-motor integration and supported the "
            "transition to a servo-based design to keep the project moving.",
        ],
        "result": [
            "Built a functional prototype that generated a real-time 180\u00b0 spatial map of "
            "surrounding objects.",
            "Adapted the design after the original stepper-motor approach could not be "
            "integrated reliably.",
            "Placed 2nd out of 19 teams in the course project.",
        ],
        "learnings": [
            "Learned the importance of rapid prototyping and early integration for identifying "
            "system-level issues sooner.",
            "Learned to stay flexible when an engineering approach does not work as intended "
            "and to adjust the design based on testing.",
            "Strengthened technical leadership by keeping a small team aligned around subsystem "
            "interfaces, testing, and a shared final system.",
        ],
        "resources": [
            {
                "title": "UltraScan Pro Final Presentation",
                "thumb": "assets/ultrascan-pro-presentation-thumb.png",
                "href": "https://docs.google.com/presentation/d/1b4-uhMS6TtqIDDbv74yqEi-dHblYmlK9EIBwr0Ur4BE/edit?usp=sharing",
            },
            {
                "title": "Video Demo of Project",
                "thumb": "assets/ultrascan-pro-video-thumb.jpg",
                "href": "https://drive.google.com/file/d/1-zwxLVknSNDsG_WgQpFIhTNE6BJzYMgk/view",
            },
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
        "summary": "Preprocessed clinical data and built and compared three MATLAB "
                   "machine-learning models (Random Forest, Gradient Boosting, and SVM) to "
                   "predict preeclampsia risk.",
        "skills": ["matlab", "ml", "datapreprocessing", "dataanalysis", "stats"],
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
        "summary": "Developed a low-cost microfluidic device for fluorescence quantification, "
                   "integrating Arduino-based sensing and controls with custom components "
                   "fabricated through laser cutting, 3D printing, and PDMS.",
        "skills": ["microfluidics", "arduino", "lasercutting", "printing", "pdms"],
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
        "summary": "Led the go-to-market strategy for SeraSwaddle, a neonatal warming device "
                   "concept, pitched the project and won 2nd place in UCI's OPEN MIC "
                   "competition.",
        "skills": ["entrepreneurship", "bizstrategy", "pitching", "riskanalysis", "meddevice"],
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
        "role": "Team Lead",
        "dates": "September 2024 – December 2024",
        "sort": "2024-09",
        "kind": "Team project",
        "summary": "Led a seven-person team through the rover project and took primary "
                   "responsibility for the final technical report, documenting the design "
                   "process, testing, and performance improvements.",
        "skills": ["leadership", "techwriting", "documentation", "testing", "solidworks"],
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
