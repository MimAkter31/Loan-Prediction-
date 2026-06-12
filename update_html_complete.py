#!/usr/bin/env python3
"""Complete HTML update to English with smaller professional boxes"""

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update about section - COMPLETE replacement
about_old = '''        <div class="mt-12 grid gap-4 sm:grid-cols-3 text-left">
          <!-- Accurate Prediction Card -->
          <div class="soft-card rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm">
            <div class="text-2xl mb-2">✓</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">নির্ভুল ভবিষ্যদ্বাণী</p>
            <p class="mt-1 text-gray-600 text-xs">সঠিক পূর্বাভাস প্রদানের জন্য মেশিন লার্নিং মডেল।</p>
          </div>

          <!-- ML Powered Card -->
          <div class="soft-card rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm">
            <div class="text-2xl mb-2">⚙️</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">এআই চালিত</p>
            <p class="mt-1 text-gray-600 text-xs">२४টি আর্থিক এবং ব্যক্তিগত বৈশিষ্ট্য বিশ্লেষণ।</p>
          </div>

          <!-- Fast Decision Card -->
          <div class="soft-card rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm">
            <div class="text-2xl mb-2">⚡</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">দ্রুত সিদ্ধান্ত</p>
            <p class="mt-1 text-gray-600 text-xs">সেকেন্ডের মধ্যে তাৎক্ষণিক সিদ্ধান্ত পান।</p>
          </div>
        </div>

        <!-- Dataset Information -->
        <div class="mt-10 grid gap-4 sm:grid-cols-3">
          <div class="rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm text-center">
            <p class="text-2xl font-bold text-indigo-600">५००००+</p>
            <p class="mt-1 text-xs text-gray-600">ডেটাসেট আকার</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm text-center">
            <p class="text-2xl font-bold text-indigo-600">२४</p>
            <p class="mt-1 text-xs text-gray-600">বৈশিষ্ট্য সংখ্যা</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-3 sm:p-4 shadow-sm text-center">
            <p class="text-2xl font-bold text-indigo-600">८९%</p>
            <p class="mt-1 text-xs text-gray-600">মডেল নির্ভুলতা</p>
          </div>
        </div>'''

about_new = '''        <div class="mt-8 grid gap-3 sm:grid-cols-3 text-left">
          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">✓</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Accurate</p>
            <p class="mt-0.5 text-gray-600 text-xs">89% prediction accuracy.</p>
          </div>

          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">⚙️</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Intelligent</p>
            <p class="mt-0.5 text-gray-600 text-xs">24+ features analyzed.</p>
          </div>

          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">⚡</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Instant</p>
            <p class="mt-0.5 text-gray-600 text-xs">Decision in seconds.</p>
          </div>
        </div>

        <div class="mt-8 grid gap-3 sm:grid-cols-3">
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">5000+</p>
            <p class="mt-0.5 text-xs text-gray-600">Records</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">24</p>
            <p class="mt-0.5 text-xs text-gray-600">Features</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">89%</p>
            <p class="mt-0.5 text-xs text-gray-600">Accuracy</p>
          </div>
        </div>'''

content = content.replace(about_old, about_new)

# Update statistics section  
stats_old = '''  <!-- Prediction Statistics Section -->
  <section class="bg-white py-16 sm:py-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-sm font-semibold tracking-wide text-indigo-600 uppercase">মডেলের কর্মক্ষমতা</p>
        <h2 class="mt-2 text-3xl sm:text-4xl font-extrabold text-gray-900">পূর্বাভাস পরিসংখ্যান</h2>
      </div>

      <div class="mt-8 grid gap-4 sm:grid-cols-3">
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-4 sm:p-5 text-center">
          <p class="text-2xl font-bold text-indigo-600">२४</p>
          <p class="mt-1 text-xs font-semibold text-gray-900">বিশ্লেষণ করা বৈশিষ্ট্য</p>
          <p class="mt-0.5 text-xs text-gray-600">আর্থিক ও ব্যক্তিগত ডেটা</p>
        </div>
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-4 sm:p-5 text-center">
          <p class="text-2xl font-bold text-green-600">९५%</p>
          <p class="mt-1 text-xs font-semibold text-gray-900">নির্ভুলতা</p>
          <p class="mt-0.5 text-xs text-gray-600">অনুমোদিত পূর্বাভাস</p>
        </div>
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-4 sm:p-5 text-center">
          <p class="text-2xl font-bold text-purple-600">🤖</p>
          <p class="mt-1 text-xs font-semibold text-gray-900">এআই চালিত</p>
          <p class="mt-0.5 text-xs text-gray-600">Random Forest</p>
        </div>
      </div>
    </div>
  </section>'''

stats_new = '''  <!-- Prediction Statistics Section -->
  <section class="bg-white py-12 sm:py-14">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-xs font-semibold tracking-wide text-indigo-600 uppercase">Performance</p>
        <h2 class="mt-2 text-2xl sm:text-3xl font-bold text-gray-900">Model Statistics</h2>
      </div>

      <div class="mt-8 grid gap-3 sm:grid-cols-3">
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-3 sm:p-3.5 text-center hover:shadow-md transition">
          <p class="text-lg font-bold text-indigo-600">24</p>
          <p class="mt-0.5 text-xs font-semibold text-gray-900">Features</p>
          <p class="mt-0.5 text-xs text-gray-600">Financial & behavioral</p>
        </div>
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-3 sm:p-3.5 text-center hover:shadow-md transition">
          <p class="text-lg font-bold text-green-600">95%</p>
          <p class="mt-0.5 text-xs font-semibold text-gray-900">Precision</p>
          <p class="mt-0.5 text-xs text-gray-600">Approval accuracy</p>
        </div>
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-3 sm:p-3.5 text-center hover:shadow-md transition">
          <p class="text-lg font-bold text-purple-600">🤖</p>
          <p class="mt-0.5 text-xs font-semibold text-gray-900">Random Forest</p>
          <p class="mt-0.5 text-xs text-gray-600">ML Algorithm</p>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(stats_old, stats_new)

# Update model details
details_old = '''  <!-- Model Details Section -->
  <section class="bg-gray-50 py-16 sm:py-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <p class="text-sm font-semibold tracking-wide text-indigo-600 uppercase text-center">प्रযুक्तिगत बिवरण</p>
        <h2 class="mt-2 text-3xl sm:text-4xl font-extrabold text-gray-900 text-center">मडेल बैশिष्ट्यसम्หूह</h2>

        <div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">अल्गोरिदम</p>
            <p class="mt-2 text-sm font-bold text-gray-900">Random Forest</p>
            <p class="mt-0.5 text-xs text-gray-600">समष्टिगत शिक्षा</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">निर्भुलता</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८९%</p>
            <p class="mt-0.5 text-xs text-gray-600">सामग्रिक निर्भुलता</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">निर्भुलता</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८७%</p>
            <p class="mt-0.5 text-xs text-gray-600">अनुमोदन पूर्वाभाव</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">पुनरुद्धार</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८५%</p>
            <p class="mt-0.5 text-xs text-gray-600">सत्य इतिबाचक</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

details_new = '''  <!-- Model Details Section -->
  <section class="bg-gray-50 py-12 sm:py-14">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <p class="text-xs font-semibold tracking-wide text-indigo-600 uppercase text-center">Technical</p>
        <h2 class="mt-2 text-2xl sm:text-3xl font-bold text-gray-900 text-center">Model Details</h2>

        <div class="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          <div class="rounded-lg bg-white border border-gray-200 p-3 shadow-sm hover:shadow-md transition">
            <p class="text-xs font-semibold text-gray-600 uppercase">Algorithm</p>
            <p class="mt-1.5 text-sm font-bold text-gray-900">Random Forest</p>
            <p class="mt-0.5 text-xs text-gray-600">Ensemble method</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-3 shadow-sm hover:shadow-md transition">
            <p class="text-xs font-semibold text-gray-600 uppercase">Accuracy</p>
            <p class="mt-1.5 text-sm font-bold text-gray-900">89%</p>
            <p class="mt-0.5 text-xs text-gray-600">Overall score</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-3 shadow-sm hover:shadow-md transition">
            <p class="text-xs font-semibold text-gray-600 uppercase">Precision</p>
            <p class="mt-1.5 text-sm font-bold text-gray-900">87%</p>
            <p class="mt-0.5 text-xs text-gray-600">Approval rate</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-3 shadow-sm hover:shadow-md transition">
            <p class="text-xs font-semibold text-gray-600 uppercase">Recall</p>
            <p class="mt-1.5 text-sm font-bold text-gray-900">85%</p>
            <p class="mt-0.5 text-xs text-gray-600">True positives</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

content = content.replace(details_old, details_new)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Complete update done!")
print("✓ About section updated to English")
print("✓ Statistics section updated to English")
print("✓ Model details section updated to English")
print("✓ All boxes made smaller and more professional")
