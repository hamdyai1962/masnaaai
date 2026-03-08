import os, re

print("[1/3] قراءة ملف المصنع الأساسي...")
file_path = r"C:\HamdyAI-Factory\dist\index.html"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("  تمت القراءة بنجاح.")
except FileNotFoundError:
    print("  خطأ: لم يتم العثور على الملف. تأكد من بناء الجزء الأول أولاً.")
    exit()

print("[2/3] حقن أكواد الوكلاء الحقيقيين (Puter AI)...")

# الكود البرمجي الفعلي (HTML + JS) الذي سيتم حقنه لبناء الوكيل
ai_agent_code = """
<div id="ai-agent-section" style="max-width: 960px; margin: 20px auto; padding: 20px; background: rgba(255,255,255,.03); border: 1px solid var(--g); border-radius: 16px; box-shadow: 0 4px 30px rgba(0, 255, 136, 0.1);">
    <h3 style="color: var(--g); margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 24px;">🤖</span> وكيل المصنع الذكي (الجيل الأول)
    </h3>
    <p style="font-size: 13px; color: var(--t2); margin-bottom: 15px;">هذا الوكيل متصل حقيقياً بمحرك Puter.js. اكتب مهمتك وسيقوم بتنفيذها.</p>
    
    <textarea id="agent-prompt" rows="4" placeholder="اطلب من الوكيل كتابة كود، تحليل نص، أو بناء خطة..." style="width: 100%; margin-bottom: 15px; resize: vertical;"></textarea>
    
    <button onclick="executeRealAgent()" class="btn btn-g" style="font-size: 14px; padding: 12px 24px;">
        ⚡ تشغيل الوكيل
    </button>
    
    <div id="agent-output-container" style="margin-top: 20px; display: none;">
        <h4 style="color: var(--t); margin-bottom: 10px; font-size: 14px;">رد الوكيل:</h4>
        <div id="agent-response" style="background: var(--bg2); padding: 15px; border-radius: 12px; border: 1px solid var(--bd); font-size: 14px; line-height: 1.6; white-space: pre-wrap;"></div>
    </div>
</div>

<script>
// المنطق البرمجي الحقيقي لتشغيل الوكيل
async function executeRealAgent() {
    const promptInput = document.getElementById('agent-prompt').value.trim();
    const responseContainer = document.getElementById('agent-output-container');
    const responseDiv = document.getElementById('agent-response');
    
    if (!promptInput) {
        alert("الرجاء كتابة مهمة للوكيل أولاً.");
        return;
    }
    
    try {
        // التحقق من تسجيل الدخول الفعلي
        const isSignedIn = await puter.auth.isSignedIn();
        if (!isSignedIn) {
            document.getElementById('puterLogin').style.display = 'block';
            return;
        }
        
        // إظهار حالة التحميل
        responseContainer.style.display = 'block';
        responseDiv.innerHTML = '<span style="color: var(--o); animation: pulse 1s infinite;">الوكيل يقوم بتحليل البيانات والتفكير... ⏳</span>';
        
        // استدعاء واجهة برمجة تطبيقات Puter للذكاء الاصطناعي بشكل حقيقي
        const aiResponse = await puter.ai.chat(promptInput);
        
        // عرض النتيجة
        responseDiv.innerHTML = '<span style="color: var(--t);">' + aiResponse.message.content + '</span>';
        
    } catch (error) {
        console.error("Agent Error:", error);
        responseDiv.innerHTML = '<span style="color: var(--r);">فشل الوكيل في إتمام المهمة: ' + error.message + '</span>';
    }
}
</script>
"""

# البحث عن المكان المناسب لحقن الكود (قبل نافذة تسجيل الدخول المخفية أو قبل نهاية الجسم)
if 'id="puterLogin"' in content:
    content = content.replace('<div id="puterLogin"', ai_agent_code + '\n<div id="puterLogin"')
elif "</body>" in content:
    content = content.replace("</body>", ai_agent_code + "\n</body>")
else:
    content = content + ai_agent_code

print("[3/3] حفظ الملفات وتحديث المصنع...")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("==========================================")
print("  ✅ تمت ترقية المصنع بنجاح!")
print("  ✅ تم دمج الوكلاء الحقيقيين (Puter.js AI)")
print("==========================================")
