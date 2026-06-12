#!/usr/bin/env python3
"""Update index.html to English with professional styling"""

# Read the file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the about section
content = content.replace(
    '''  <section id="about" class="bg-gray-50 py-16 sm:py-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-sm font-semibold tracking-wide text-indigo-600 uppercase">আমাদের সম্পর্কে</p>
        <h2 class="mt-2 text-3xl sm:text-4xl font-extrabold text-gray-900">বাংলাদেশ ঋণ ভবিষ্যদ্বাণী ব্যবস্থা</h2>
        <p class="mt-4 text-lg text-gray-600 max-w-3xl mx-auto">
          এই প্রকল্প আবেদনকারীর আর্থিক তথ্য, আচরণগত ডেটা এবং ক্রেডিট সূচক ব্যবহার করে ঋণ অনুমোদনের ঝুঁকি মূল্যায়ন করে। লক্ষ্য হল দ্রুত এবং নির্ভরযোগ্য স্ক্রিনিং প্রক্রিয়া সমর্থন করা।
        </p>

        <div class="mt-12 grid gap-4 sm:grid-cols-3 text-left">
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
            <p class="text-2xl font-bold text-indigo-600">५०००+</p>
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
        </div>
      </div>
    </div>
  </section>''',
    '''  <section id="about" class="bg-gray-50 py-12 sm:py-14">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-xs font-semibold tracking-wide text-indigo-600 uppercase">About</p>
        <h2 class="mt-2 text-2xl sm:text-3xl font-bold text-gray-900">Why Choose Our Solution</h2>
        <p class="mt-3 text-sm text-gray-600 max-w-3xl mx-auto">
          Leveraging machine learning to assess loan approval risk with precision. Complete analysis across 24+ financial features.
        </p>

        <div class="mt-8 grid gap-3 sm:grid-cols-3 text-left">
          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">✓</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Accurate</p>
            <p class="mt-0.5 text-gray-600 text-xs">89% prediction accuracy with Random Forest.</p>
          </div>

          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">⚙️</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Intelligent</p>
            <p class="mt-0.5 text-gray-600 text-xs">Analyzes financial and behavioral patterns.</p>
          </div>

          <div class="soft-card rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm hover:shadow-md transition">
            <div class="text-lg mb-1">⚡</div>
            <p class="text-xs font-semibold text-indigo-600 uppercase">Instant</p>
            <p class="mt-0.5 text-gray-600 text-xs">Loan decision in seconds.</p>
          </div>
        </div>

        <div class="mt-8 grid gap-3 sm:grid-cols-3">
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">5000+</p>
            <p class="mt-0.5 text-xs text-gray-600">Training Records</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">24</p>
            <p class="mt-0.5 text-xs text-gray-600">Features</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-2.5 sm:p-3 shadow-sm text-center hover:shadow-md transition">
            <p class="text-lg font-bold text-indigo-600">89%</p>
            <p class="mt-0.5 text-xs text-gray-600">Accuracy</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''
)

# Replace statistics section
content = content.replace(
    '''  <!-- Prediction Statistics Section -->
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
  </section>''',
    '''  <!-- Prediction Statistics Section -->
  <section class="bg-white py-12 sm:py-14">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-xs font-semibold tracking-wide text-indigo-600 uppercase">Performance</p>
        <h2 class="mt-2 text-2xl sm:text-3xl font-bold text-gray-900">Model Statistics</h2>
      </div>

      <div class="mt-8 grid gap-3 sm:grid-cols-3">
        <div class="soft-card rounded-lg bg-indigo-50 border border-indigo-100 p-3 sm:p-3.5 text-center hover:shadow-md transition">
          <p class="text-lg font-bold text-indigo-600">24</p>
          <p class="mt-0.5 text-xs font-semibold text-gray-900">Features Analyzed</p>
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
          <p class="mt-0.5 text-xs text-gray-600">Ensemble learning</p>
        </div>
      </div>
    </div>
  </section>'''
)

# Replace model details section
content = content.replace(
    '''  <!-- Model Details Section -->
  <section class="bg-gray-50 py-16 sm:py-20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <p class="text-sm font-semibold tracking-wide text-indigo-600 uppercase text-center">প্রযুক্তিগত বিবরণ</p>
        <h2 class="mt-2 text-3xl sm:text-4xl font-extrabold text-gray-900 text-center">মডেল বৈশিষ্ট্যসমূহ</h2>

        <div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">অ্যালগরিদম</p>
            <p class="mt-2 text-sm font-bold text-gray-900">Random Forest</p>
            <p class="mt-0.5 text-xs text-gray-600">সমষ্টিগত শিক্ষা</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">नির्ভुलता</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८९%</p>
            <p class="mt-0.5 text-xs text-gray-600">সামগ্রিক নির্ভুলতা</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">नির्ভुलतা</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८७%</p>
            <p class="mt-0.5 text-xs text-gray-600">অনুমোদন পূর্বাভাস</p>
          </div>
          <div class="rounded-lg bg-white border border-gray-200 p-4 shadow-sm">
            <p class="text-xs font-semibold text-gray-600 uppercase">पुनरुद्धार</p>
            <p class="mt-2 text-sm font-bold text-gray-900">८५%</p>
            <p class="mt-0.5 text-xs text-gray-600">সত্য ইতিবাচক</p>
          </div>
        </div>
      </div>
    </div>
  </section>''',
    '''  <!-- Model Details Section -->
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
)

# Replace team member boxes (smaller and more professional)
content = content.replace(
    'rounded-2xl border border-gray-200 p-5 sm:p-6 shadow-sm bg-gray-50',
    'rounded-lg border border-gray-200 p-3.5 sm:p-4 shadow-sm bg-white'
)

# Replace team member heading sizes
content = content.replace(
    'text-xl sm:text-2xl font-bold text-gray-900',
    'text-lg font-bold text-gray-900'
)

# Update contact section heading
content = content.replace(
    'আমাদের সাথে যোগাযোগ করুন। আমরা আপনার প্রশ্ন এবং মতামতের জন্য অপেক্ষা করছি।',
    'Have any questions? We&rsquo;d love to hear from you. Reach out anytime and we&rsquo;ll respond as quickly as possible.'
)

# Update contact info labels
content = content.replace(
    '<p class="text-sm font-semibold text-gray-900">যোগাযোগ তথ্য</p>',
    '<p class="text-sm font-semibold text-gray-900">Contact Information</p>'
)

content = content.replace(
    '<span class="font-semibold text-gray-900">📧 ইমেইল 1:</span>',
    '<span class="font-semibold text-gray-900">📧 Primary Email:</span>'
)

content = content.replace(
    '<span class="font-semibold text-gray-900">📧 ইমেইল 2:</span>',
    '<span class="font-semibold text-gray-900">📧 Secondary Email:</span>'
)

content = content.replace(
    '<span class="font-semibold text-gray-900">⏱️ সাড়া দেওয়ার সময়:</span> २४ ঘন্টার মধ্যে',
    '<span class="font-semibold text-gray-900">⏱️ Response Time:</span> Within 24 hours'
)

# Update form labels
content = content.replace(
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="first_name">প্রথম নাম</label>',
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="first_name">First Name</label>'
)

content = content.replace(
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="last_name">শেষ নাম</label>',
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="last_name">Last Name</label>'
)

content = content.replace(
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="email">কর্ম ইমেইল</label>',
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="email">Email Address</label>'
)

content = content.replace(
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="message">বার্তা</label>',
    '<label class="block text-sm font-medium text-gray-700 mb-2" for="message">Message</label>'
)

content = content.replace(
    'placeholder="আপনার প্রথম নাম"',
    'placeholder="John"'
)

content = content.replace(
    'placeholder="আপনার শেষ নাম"',
    'placeholder="Doe"'
)

content = content.replace(
    'placeholder="আপনার ইমেইল ঠিকানা"',
    'placeholder="john@example.com"'
)

content = content.replace(
    'placeholder="আপনার বার্তা এখানে লিখুন"',
    'placeholder="Your message here..."'
)

content = content.replace(
    '          বার্তা পাঠান',
    '          Send Message'
)

# Write the updated content
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ index.html updated successfully!")
print("✓ All content converted to English")
print("✓ Professional compact styling applied")
print("✓ Smaller boxes and reduced padding")
