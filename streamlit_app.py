import streamlit as st
import streamlit.components.v1 as components

# إعدادات صفحة ستريمليت
st.set_page_config(
    page_title="البوابة الذكية الشاملة لتاريخ وأرشيف كرة القدم العالمية (حتى 2023)",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ البوابة الذكية الشاملة لتاريخ وأرشيف كرة القدم العالمية (حتى 2023)")
st.markdown("استعراض تفاعلي احترافي يوثق البيانات، السجلات، والإحصائيات التاريخية لعالم كرة القدم حتى عام 2023.")

# كود HTML و CSS الخاص بالعرض التقديمي مع الخطوط المطورة
presentation_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>البوابة الذكية الشاملة لتاريخ وأرشيف كرة القدم العالمية (حتى 2023)</title>
    <!-- Google Fonts: Alexandria & Plus Jakarta Sans for ultra-premium typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;600;700;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            background-color: #0b132b;
            display: grid;
            gap: 20px;
            grid-template-columns: 1fr;
            margin: 0;
            min-height: 100vh;
            padding: 20px 0;
            place-items: center;
        }

        .slide-container {
            align-items: center;
            background-color: #1c2541;
            border-radius: 12px;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
            display: flex;
            flex-direction: column;
            font-family: 'Alexandria', 'Tajawal', sans-serif;
            height: 720px;
            justify-content: center;
            overflow: hidden;
            padding: 50px;
            position: relative;
            width: 1280px;
            color: #e0e1dd;
        }

        .slide-container::before {
            content: '';
            height: 100%;
            left: 0;
            position: absolute;
            top: 0;
            width: 100%;
            z-index: 0;
            background: radial-gradient(circle at top right, rgba(5, 150, 105, 0.15), transparent 50%);
        }

        .slide-container > * {
            position: relative;
            z-index: 1;
        }

        .slide-container h1,
        .slide-container h2,
        .slide-container h3 {
            color: #ffffff;
            font-family: 'Alexandria', sans-serif;
            font-weight: 700;
            margin: 0;
        }

        .slide-container p,
        .slide-container li,
        .slide-container .subtitle,
        .slide-container th,
        .slide-container td {
            color: #b8c1ec;
            font-family: 'Alexandria', sans-serif;
            font-size: 18px;
            line-height: 1.6;
        }

        .slide-container h1 {
            font-size: 48px;
            line-height: 1.3;
            color: #ffffff;
        }

        .slide-container .slide-title {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 30px;
            text-align: right;
            width: 100%;
            color: #64dfdf;
            border-bottom: 2px solid rgba(100, 223, 223, 0.2);
            padding-bottom: 10px;
        }

        .slide-container .subtitle {
            font-size: 20px;
            color: #8d99ae;
            margin-top: 20px;
            line-height: 1.6;
        }

        .content-area {
            align-items: center;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
            justify-content: center;
            width: 100%;
        }

        .title-layout {
            text-align: center;
            max-width: 1100px;
        }

        .title-layout .badge {
            background-color: #059669;
            color: #ffffff;
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 16px;
            font-weight: 700;
            display: inline-block;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
        }

        .section-title-layout {
            text-align: center;
            width: 100%;
        }

        .section-title-layout h2 {
            font-size: 46px;
            color: #ffffff;
            margin-bottom: 15px;
        }

        .section-title-layout hr {
            background-color: #059669;
            border: none;
            height: 4px;
            margin: 20px auto;
            width: 80px;
            border-radius: 2px;
        }

        .two-column {
            align-items: center;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            width: 100%;
        }

        .two-column.tiled > div {
            background-color: #111827;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 35px;
            text-align: right;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        .image-wrapper {
            border-radius: 12px;
            height: 350px;
            max-width: 100%;
            overflow: hidden;
            width: 100%;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }

        .image-wrapper img {
            height: 100%;
            max-width: 100%;
            object-fit: cover;
            width: 100%;
        }

        .tiled-content {
            align-items: stretch;
            display: flex;
            gap: 30px;
            justify-content: center;
            width: 100%;
        }

        .tile {
            align-items: flex-start;
            background-color: #111827;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            flex: 1;
            padding: 30px;
            text-align: right;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        .tile .icon {
            color: #059669;
            font-size: 40px;
            margin-bottom: 20px;
            background: rgba(5, 150, 105, 0.1);
            padding: 15px;
            border-radius: 10px;
        }

        .tile h3 {
            color: #ffffff;
            font-size: 22px;
            margin-bottom: 10px;
        }

        .bullet-list {
            max-width: 1000px;
            width: 100%;
        }

        .bullet-list ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .bullet-list li {
            gap: 15px;
            margin-bottom: 20px;
            padding-right: 40px;
            position: relative;
        }

        .bullet-list i {
            color: #059669;
            font-size: 22px;
            right: 0;
            position: absolute;
            top: 4px;
        }

        .highlight-numbers-layout > div:first-child {
            text-align: center;
            background: linear-gradient(135deg, #111827, #1f2937);
            padding: 40px;
            border-radius: 16px;
            border: 1px solid rgba(5, 150, 105, 0.3);
        }

        .highlight-numbers-layout .number {
            color: #64dfdf;
            font-size: 80px;
            font-weight: 900;
            font-family: 'Plus Jakarta Sans', sans-serif;
            line-height: 1;
            margin-bottom: 10px;
        }

        .highlight-numbers-layout .number-label {
            font-size: 20px;
            color: #ffffff;
            font-weight: 700;
        }

        .slide-container.bleed-image-layout {
            align-items: start;
            display: grid;
            gap: 0;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            padding: 0;
        }

        .slide-container.bleed-image-layout > .content-container {
            padding: 60px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .slide-container.bleed-image-layout > .image-container {
            height: 100%;
            overflow: hidden;
            width: 100%;
        }

        .slide-container.bleed-image-layout img.bleed-image-side {
            display: block;
            height: 720px;
            object-fit: cover;
            width: 100%;
        }

        .image-tile {
            flex: 1;
            text-align: center;
            background: #111827;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .image-tile .image-wrapper {
            height: 200px;
            margin-bottom: 15px;
        }

        .table-layout {
            width: 100%;
            background: #111827;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .table-layout table {
            border-collapse: collapse;
            width: 100%;
        }

        .table-layout th,
        .table-layout td {
            border-bottom: 1px solid rgba(255,255,255,0.08);
            padding: 16px 20px;
            text-align: right;
        }

        .table-layout th {
            background-color: #1f2937;
            color: #64dfdf;
            font-size: 18px;
            font-weight: 700;
        }

        .chart-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
            background: #111827;
            padding: 30px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .bar {
            align-items: center;
            display: flex;
            gap: 20px;
        }

        .bar .label {
            color: #ffffff;
            flex: 0 0 180px;
            font-weight: 700;
            text-align: right;
        }

        .bar .bar-inner {
            background-color: #1f2937;
            border-radius: 6px;
            flex-grow: 1;
            height: 36px;
            overflow: hidden;
        }

        .bar .bar-fill {
            align-items: center;
            border-radius: 6px;
            color: white;
            display: flex;
            font-size: 16px;
            font-weight: 700;
            height: 100%;
            justify-content: flex-start;
            padding-left: 15px;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .full-bg-image {
            background-position: center;
            background-size: cover;
            text-align: center;
        }

        .full-bg-image .content-overlay {
            background: rgba(15, 23, 42, 0.85);
            padding: 50px 80px;
            border-radius: 20px;
            max-width: 900px;
            border: 1px solid rgba(100, 223, 223, 0.3);
        }

        .qa-layout {
            text-align: center;
            width: 100%;
        }

        .qa-layout h2 {
            font-size: 60px;
            color: #64dfdf;
            margin-bottom: 20px;
        }

        .qa-layout p {
            font-size: 22px;
        }

        .qa-layout .contact-info {
            color: #059669;
            font-size: 20px;
            margin-top: 30px;
            font-weight: 700;
        }
    </style>
</head>
<body>

<!-- Slide 1: Title_Slide -->
<div class="slide-container" id="slide1">
    <div class="title-layout">
        <div class="badge">الأرشيف الرقمي الاحترافي</div>
        <h1>البوابة الذكية الشاملة لتاريخ وأرشيف كرة القدم العالمية (حتى 2023)</h1>
        <p class="subtitle">المرجع الموثق للبيانات، الإحصائيات، وسجلات البطولات حتى عام 2023</p>
    </div>
</div>

<!-- Slide 2: Section_Title -->
<div class="slide-container" id="slide2">
    <div class="section-title-layout">
        <hr>
        <h2>نظرة عامة على المنظومة والبيانات التاريخية</h2>
        <p class="subtitle">توثيق علمي شامل لبطولات الأندية والمنتخبات العالمية</p>
    </div>
</div>

<!-- Slide 3: Image_Right_Text_Left -->
<div class="slide-container" id="slide3">
    <h2 class="slide-title">شمولية الأرشيف حتى عام 2023</h2>
    <div class="content-area">
        <div class="two-column">
            <div>
                <p>تقدم البوابة الذكية أرشيفاً مترابطاً ومتكاملًا يعيد صياغة تاريخ كرة القدم العالمية منذ انطلاقتها وحتى نهاية عام 2023.</p>
                <p>تغطي البيانات تقارير الفيفا الرسمية، سجلات اللاعبين، البطولات القارية، وانتقالات النجوم التاريخية مع دقة متناهية في المراجع والمصادر الإحصائية المعتمدة.</p>
            </div>
            <div>
                <div class="image-wrapper">
                    <img alt="historic football stadium with crowd and lights" src="https://auburntigers.com/imgproxy/8LezwRtGAmuFVy-hIFbMsDSEROerWL0LueyiCdA-SYo/rs:fit:1980:0:0:0/g:ce:0:0/q:90/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2F1YnVybi1wcm9kLzIwMjYvMDYvMTAvcDdLVXdkMzlSWW9DQ094NUpHZTFLb3VYNDhkV2ZZa29pY3k3Q0xPRS5qcGc.jpg">
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Slide 4: Tiled_Text_With_Icons -->
<div class="slide-container" id="slide4">
    <h2 class="slide-title">محاور الأرشيف الرئيسية</h2>
    <div class="content-area">
        <div class="tiled-content">
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-users"></i></div>
                <h3>قاعدة بيانات اللاعبين</h3>
                <p>توثيق شامل لأكثر من 128 ألف لاعب محترف عبر مئات الأندية والاتحادات المحلية والعالمية.</p>
            </div>
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-trophy"></i></div>
                <h3>البطولات والمسابقات</h3>
                <p>أرشيف تفصيلي لكافة البطولات الدولية والمحلية الكبرى مع سرد النتائج والمباريات النهائية.</p>
            </div>
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-chart-line"></i></div>
                <h3>الإحصائيات المتقدمة</h3>
                <p>تحليلات دقيقة لأبرز الأرقام القياسية والأهداف التاريخية المسجلة حتى ختام موسم 2023.</p>
            </div>
        </div>
    </div>
</div>

<!-- Slide 5: Bleed_Image_Right -->
<div class="slide-container bleed-image-layout" id="slide5">
    <div class="content-container">
        <h2 class="slide-title">عصر الأساطير والإنجازات</h2>
        <p>شهدت السنوات حتى 2023 تنافسًا تاريخيًا غير مسبوق بين أساطير المستديرة مثل كريستيانو رونالدو وليونيل ميسي وغيرهم.</p>
        <p>يوثق الأرشيف تفاصيل مذهلة عن الأهداف، الأرقام القياسية، والتتويجات التي صنعت تاريخ اللعبة الحديث.</p>
    </div>
    <div class="image-container">
        <img class="bleed-image-side" alt="football player celebrating on pitch stadium lights" src="https://theboyhotspur.com/wp-content/uploads/2026/07/spurs-land-mateus-fernandes-85m-record-signing.webp">
    </div>
</div>

<!-- Slide 6: Highlighted_Numbers -->
<div class="slide-container" id="slide6">
    <h2 class="slide-title">أرقام قياسية في لغة الأرقام</h2>
    <div class="content-area">
        <div class="two-column highlight-numbers-layout">
            <div>
                <div class="number">128K+</div>
                <div class="number-label">لاعب محترف موثق في الأرشيف العالمي</div>
            </div>
            <div>
                <h3 style="color: #64dfdf; font-size: 26px; margin-bottom: 15px;">دقة وبنية متكاملة للبيانات</h3>
                <p>تضم قاعدة البيانات أكثر من 3,986 نادياً محترفاً في 135 دولة، مع رصد كامل لبيانات الانتقالات والبطولات والتصنيفات التاريخية.</p>
            </div>
        </div>
    </div>
</div>

<!-- Slide 7: Styled_Bullet_Points -->
<div class="slide-container" id="slide7">
    <h2 class="slide-title">مميزات البوابة الذكية</h2>
    <div class="content-area">
        <div class="bullet-list">
            <ul>
                <li><i class="fa-solid fa-circle-check"></i><strong>بحث فوري ومتقدم:</strong> استرجاع سريع لأي مباراة أو بطولة أو لاعب تاريخي بضغطة زر واحدة.</li>
                <li><i class="fa-solid fa-circle-check"></i><strong>مقارنات شاملة:</strong> أدوات متطورة لمقارنة إحصائيات المنتخبات والأندية واللاعبين عبر العصور المختلفة حتى 2023.</li>
                <li><i class="fa-solid fa-circle-check"></i><strong>توثيق موثوق:</strong> اعتماد البيانات على تقارير الفيفا والأرشيف الدولي المعتمد لضمان دقة المعلومات.</li>
                <li><i class="fa-solid fa-circle-check"></i><strong>واجهة تفاعلية ذكية:</strong> تصميم عصري يجمع بين جمال الشكل وسهولة الاستخدام للمهتمين والباحثين.</li>
            </ul>
        </div>
    </div>
</div>

<!-- Slide 8: Tiled_Images -->
<div class="slide-container" id="slide8">
    <h2 class="slide-title">محطات كبرى في الأرشيف</h2>
    <div class="content-area">
        <div class="tiled-content">
            <div class="image-tile">
                <div class="image-wrapper"><img alt="football trophy closeup" src="https://images.unsplash.com/photo-1637203723757-a9b26181e1ad?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0"></div>
                <h3 style="color:#ffffff; font-size:18px; margin-bottom:5px;">سجلات البطولات</h3>
                <p style="font-size:15px;">أرشيف تفصيلي لكؤوس العالم والبطولات القارية.</p>
            </div>
            <div class="image-tile">
                <div class="image-wrapper"><img alt="football match action shot" src="https://miro.medium.com/v2/resize:fit:1400/1*0PkLKWx4A5-kJHV6SVbFGg.jpeg"></div>
                <h3 style="color:#ffffff; font-size:18px; margin-bottom:5px;">مباريات تاريخية</h3>
                <p style="font-size:15px;">توثيق أهم المباريات الحاسمة والمواجهات الخالدة.</p>
            </div>
            <div class="image-tile">
                <div class="image-wrapper"><img alt="historic football equipment" src="https://fanatics.frgimages.com/cleveland-browns/cleveland-browns-historic-logo-womens-embroidered-cowboy-boots-brown_pi1188000_altimages_ff_1188127alt5_full.jpg?_hv=2&w=1018"></div>
                <h3 style="color:#ffffff; font-size:18px; margin-bottom:5px;">تطور اللعبة</h3>
                <p style="font-size:15px;">تاريخ الكرة والأدوات المستخدمة منذ نشأة الرياضة.</p>
            </div>
        </div>
    </div>
</div>

<!-- Slide 9: Table -->
<div class="slide-container" id="slide9">
    <h2 class="slide-title">مقارنة نطاق البيانات التاريخية</h2>
    <div class="content-area">
        <div class="table-layout">
            <table>
                <thead>
                    <tr>
                        <th>الفئة المستهدفة</th>
                        <th>النطاق التاريخي</th>
                        <th>مستوى التوثيق</th>
                        <th>المصدر الرئيسي</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>بطولات كأس العالم</strong></td>
                        <td>1930 - 2022</td>
                        <td>شامل ومفصل لكل المباريات</td>
                        <td>أرشيف الفيفا الرسمي</td>
                    </tr>
                    <tr>
                        <td><strong>دوريات الأندية الكبرى</strong></td>
                        <td>حتى عام 2023</td>
                        <td>إحصائيات الأهداف واللاعبين</td>
                        <td>قواعد البيانات الدولية المعتمدة</td>
                    </tr>
                    <tr>
                        <td><strong>الجوائز الفردية</strong></td>
                        <td>حتى عام 2023</td>
                        <td>سجل الفائزين والأرقام القياسية</td>
                        <td>التقارير السنوية الموثقة</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- Slide 10: Bar_Chart_For_Comparisons -->
<div class="slide-container" id="slide10">
    <h2 class="slide-title">أبرز الهدافين والأرقام (حتى 2023)</h2>
    <div class="content-area">
        <div class="chart-container">
            <div class="bar">
                <div class="label">كريستيانو رونالدو</div>
                <div class="bar-inner"><div class="bar-fill" style="width: 100%; background: linear-gradient(90deg, #059669, #34d399);">54 هدف (2023)</div></div>
            </div>
            <div class="bar">
                <div class="label">كيليان مبابي</div>
                <div class="bar-inner"><div class="bar-fill" style="width: 96%; background: linear-gradient(90deg, #0284c7, #38bdf8);">52 هدف (2023)</div></div>
            </div>
            <div class="bar">
                <div class="label">هاري كين</div>
                <div class="bar-inner"><div class="bar-fill" style="width: 96%; background: linear-gradient(90deg, #d97706, #fbbf24);">52 هدف (2023)</div></div>
            </div>
            <div class="bar">
                <div class="label">إيرلينغ هالاند</div>
                <div class="bar-inner"><div class="bar-fill" style="width: 92%; background: linear-gradient(90deg, #7c3aed, #a78bfa);">50 هدف (2023)</div></div>
            </div>
        </div>
        <p style="margin-top: 15px; font-size: 16px; text-align: center;">إحصائيات الأهداف المسجلة خلال عام 2023 على مستوى الأندية والمنتخبات ضمن الأرشيف العالمي.</p>
    </div>
</div>

<!-- Slide 11: Full_Background_Image -->
<div class="slide-container full-bg-image" id="slide11" style="background-image: url('https://inspiredby.luxury/wp-content/uploads/2026/07/ibl-travel-09-hero-stadium-night.jpg');">
    <div class="content-overlay">
        <h2 style="font-size:42px; color: #64dfdf; margin-bottom: 15px;">مستقبل الأرشفة والتحليل الرياضي</h2>
        <p>دمج أحدث تقنيات قواعد البيانات الذكية لاستعراض التاريخ الكروي العالمي بدقة متناهية، ليكون المرجع الأول لكل باحث ومشجع رياضي.</p>
    </div>
</div>

<!-- Slide 12: Q&A -->
<div class="slide-container" id="slide12">
    <div class="qa-layout">
        <h2>شكراً لحسن استماعكم</h2>
        <p>نتطلع لخدمتكم واستكشاف أرشيف كرة القدم العالمية سوياً.</p>
        <div class="contact-info">
            www.football-archive-gateway.com | info@football-archive.com
        </div>
    </div>
</div>

</body>
</html>
"""

# عرض الـ HTML داخل Streamlit باستخدام component iframe
components.html(presentation_html, height=780, scrolling=True)
