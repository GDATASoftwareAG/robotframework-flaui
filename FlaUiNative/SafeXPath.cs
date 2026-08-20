using System;
using System.Reflection;
using System.Runtime.ExceptionServices;
using System.Security;

namespace FlaUiNative
{
    /// <summary>
    /// Invokes FlaUI XPath lookups through reflection so AccessViolationException
    /// from UI Automation tree walking is wrapped as a catchable InvalidOperationException
    /// instead of crashing the Python process.
    /// </summary>
    public static class SafeXPath
    {
        [HandleProcessCorruptedStateExceptions]
        [SecurityCritical]
        public static object FindFirstByXPath(object element, string xpath)
        {
            return Invoke(element, "FindFirstByXPath", xpath);
        }

        [HandleProcessCorruptedStateExceptions]
        [SecurityCritical]
        public static object FindAllByXPath(object element, string xpath)
        {
            return Invoke(element, "FindAllByXPath", xpath);
        }

        [HandleProcessCorruptedStateExceptions]
        [SecurityCritical]
        private static object Invoke(object element, string methodName, string xpath)
        {
            if (element == null)
            {
                return null;
            }

            try
            {
                var method = element.GetType().GetMethod(methodName, new[] { typeof(string) });
                if (method == null)
                {
                    throw new MissingMethodException(methodName);
                }

                return method.Invoke(element, new object[] { xpath });
            }
            catch (TargetInvocationException ex)
            {
                throw new InvalidOperationException("XPath lookup failed.", ex.InnerException ?? ex);
            }
            catch (AccessViolationException ex)
            {
                throw new InvalidOperationException("XPath lookup failed.", ex);
            }
        }
    }
}
